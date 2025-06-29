from warnings import deprecated

from django.db import IntegrityError
from django.utils import timezone
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.serializers import ModelSerializer

from apps.core.exceptions import DetailedValidationException
from apps.organizations.models import Organization


class OrganizationMixin(GenericAPIView):
    def get_organization(self):
        return get_object_or_404(Organization, id=self.kwargs["organization_id"])

    def get_queryset(self):
        queryset = super().get_queryset()
        organization = self.get_organization()
        return queryset.filter(organization=organization)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["organization"] = self.get_organization()
        return context


@deprecated("Use OrgPrimaryKeyRelatedField instead")
class OrganizationQuerysetMixin(ModelSerializer):
    organization_related_fields = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        organization = self.context.get("organization")

        if organization:
            request = getattr(self.context.get("request"), "method", None)
            if not request or request in ["POST", "PUT", "PATCH"]:
                for field_name, model_class in self.organization_related_fields.items():
                    if field_name in self.fields:
                        self.fields[field_name].queryset = model_class.objects.filter(
                            organization=organization
                        )


class UniqueFieldsValidatorMixin(ModelSerializer):
    unique_fields = []

    def validate(self, data):
        data = super().validate(data)

        filters = self.get_unique_filters(data)

        if filters is None:
            return data

        queryset = self.get_existing_queryset(filters)

        if queryset.exists():
            raise self.get_exception()

        return data

    def get_unique_filters(self, data):
        filters = {field: data.get(field) for field in self.unique_fields}

        if None in filters.values():
            return None

        organization = self.context.get("organization")
        if organization:
            filters["organization"] = organization

        return filters

    def get_existing_queryset(self, filters):
        model = self.Meta.model
        queryset = model.objects.filter(**filters)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        return queryset

    def get_exception(self):
        model = self.Meta.model

        if len(self.unique_fields) == 1:
            field_name = self.unique_fields[0]
            msg = f"A {model.__name__} with this field ({field_name}) already exists."
        else:
            fields = ", ".join([f"{field}" for field in self.unique_fields])
            msg = f"{model.__name__} with these fields ({fields}) already exists."
        return DetailedValidationException(
            msg,
            code=f"{model.__name__}_already_exists",
        )


class AutoCreateRelatedModelMixin(ModelSerializer):
    creation_required_fields = []

    def validate(self, data):
        data = super().validate(data)

        field_name = self.get_creation_attr("creation_field_name")
        model = self.get_creation_attr("creation_model")

        if not field_name or not model:
            raise DetailedValidationException(
                message="field_name and model cannot be None",
                code="creation_fields_empty",
            )

        if self.is_related_empty(data, field_name):
            data[field_name] = self.create_related_instance(data, model)

        return data

    def get_creation_attr(self, name):
        return getattr(self, name, None) or getattr(self.__class__, name, None)

    def is_related_empty(self, data, field_name):
        related_instance = data.get(field_name)
        return not related_instance

    def get_creation_data(self, data, model):
        creation_data = {}

        for field in self.creation_required_fields:
            if field in data:
                creation_data[field] = data[field]
            elif field in self.initial_data:
                creation_data[field] = self.initial_data[field]
            else:
                raise DetailedValidationException(
                    message=f"Field ({field}) is required to auto-create {model.__name__}.",
                    code=f"{model.__name__}_requires_{field}",
                )

        return creation_data

    def create_related_instance(self, data, model):
        creation_data = self.get_creation_data(data, model)

        organization = self.context.get("organization")
        if organization and "organization" in [
            field.name for field in model._meta.fields
        ]:
            creation_data["organization"] = organization

        if "number" in [field.name for field in model._meta.fields]:
            year_suffix = timezone.now().strftime("%y")
            count = model.objects.filter(organization=organization).count() + 1
            creation_data["number"] = f"СД-{count:04d}/{year_suffix}"

        try:
            return model.objects.create(**creation_data)
        except IntegrityError as e:
            raise DetailedValidationException(
                message=f"Failed to auto-create {model.__name__}: {str(e)}",
                code=f"{model.__name__.lower()}_creation_failed",
            )
