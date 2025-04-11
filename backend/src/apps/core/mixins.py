from django.utils import timezone
from django.db import IntegrityError
from rest_framework.serializers import ModelSerializer

from apps.core.exceptions import DetailedValidationException
from apps.organizations.models import Organization
from rest_framework.generics import get_object_or_404, GenericAPIView


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

        model = self.Meta.model
        filters = {field: data.get(field) for field in self.unique_fields}

        if None in filters.values():
            return data

        organization = self.context.get("organization")

        if organization:
            filters["organization"] = organization

        queryset = model.objects.filter(**filters)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            if len(self.unique_fields) == 1:
                field_name = self.unique_fields[0]
                msg = (
                    f"A {model.__name__} with this field ({field_name}) already exists."
                )
            else:
                fields = ", ".join([f"{field}" for field in self.unique_fields])
                msg = f"{model.__name__} with these fields ({fields}) already exists."
            raise DetailedValidationException(
                msg,
                code=f"{model.__name__}_already_exists",
            )

        return data


class AutoCreateRelatedModelMixin(ModelSerializer):
    auto_create_flag_field = "create_related_automatically"
    creation_required_fields = []

    def validate(self, data):
        data = super().validate(data)

        field_name = getattr(self, "creation_field_name", None) or getattr(
            self.__class__, "creation_field_name", None
        )
        model = getattr(self, "creation_model", None) or getattr(
            self.__class__, "creation_model", None
        )

        if not field_name or not model:
            raise DetailedValidationException(
                message="field_name and model cannot be None",
                code="creation_fields_empty",
            )

        create_flag = self.initial_data.get(self.auto_create_flag_field)
        related_instance = data.get(field_name)

        if not related_instance and str(create_flag).lower() == "true":
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
                related_instance = model.objects.create(**creation_data)
            except IntegrityError as e:
                raise DetailedValidationException(
                    message=f"Failed to auto-create {model.__name__}: {str(e)}",
                    code=f"{model.__name__.lower()}_creation_failed",
                )

            data[field_name] = related_instance

        return data
