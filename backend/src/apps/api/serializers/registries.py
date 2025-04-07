from rest_framework import serializers

from apps.core.mixins import UniqueFieldsValidatorMixin, OrganizationQuerysetMixin
from apps.core.serializers import BaseOrganizationModelSerializer
from apps.registries.models import Category, Manufacturer, Color, MeasurementUnit


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
