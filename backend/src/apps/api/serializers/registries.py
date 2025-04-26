from rest_framework import serializers

from apps.core.mixins import UniqueFieldsValidatorMixin, OrganizationQuerysetMixin
from apps.core.serializers import BaseOrganizationModelSerializer
from apps.registries.models import (
    Category,
    Manufacturer,
    Color,
    MeasurementUnit,
    Workplace,
    HourlyWage,
)


class CategorySerializer(
    OrganizationQuerysetMixin,
    UniqueFieldsValidatorMixin,
    BaseOrganizationModelSerializer,
):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.none(), allow_null=True, required=False
    )
    subcategories = serializers.SerializerMethodField()

    organization_related_fields = {
        "parent": Category,
    }
    unique_fields = ["name"]

    class Meta:
        model = Category
        fields = ("id", "name", "parent", "subcategories", "created_at", "updated_at")

    def get_subcategories(self, obj):
        serializer = self.__class__(
            obj.subcategories.all(), many=True, context=self.context
        )
        return serializer.data


class ManufacturerSerializer(
    UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer
):
    unique_fields = ["name"]

    class Meta:
        model = Manufacturer
        fields = ("id", "name", "description", "created_at", "updated_at")


class ColorSerializer(UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer):
    unique_fields = ["name"]

    class Meta:
        model = Color
        fields = ("id", "name", "code", "hex", "created_at", "updated_at")


class MeasurementUnitSerializer(
    UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer
):
    unique_fields = ["unit", "abbreviation"]

    class Meta:
        model = MeasurementUnit
        fields = ("id", "unit", "abbreviation", "okei_code", "created_at", "updated_at")


class WorkplaceSerializer(UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer):
    color = serializers.RegexField(regex=r"^#(?:[0-9a-fA-F]{3}){1,2}$")

    unique_fields = ["name"]

    class Meta:
        model = Workplace
        fields = (
            "id",
            "icon",
            "name",
            "description",
            "color",
            "created_at",
            "updated_at",
        )


class HourlyWageSerializer(UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer):
    unique_fields = ["name"]

    class Meta:
        model = HourlyWage
        fields = (
            "id",
            "name",
            "wage",
            "created_at",
            "updated_at",
        )
