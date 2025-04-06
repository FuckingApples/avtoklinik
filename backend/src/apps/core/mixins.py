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


class UniqueFieldsValidatorMixin(ModelSerializer):
    unique_fields = []

    def validate(self, data):
        model = self.Meta.model
        filters = {field: data.get(field) for field in self.unique_fields}

        if None in filters.values():
            return data

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
