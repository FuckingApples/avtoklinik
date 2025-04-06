from rest_framework import serializers

from apps.core.mixins import UniqueFieldsValidatorMixin, OrganizationQuerysetMixin
from apps.core.serializers import BaseOrganizationModelSerializer
from apps.registries.models import Category, Manufacturer, Color, MeasurementUnit


class CategorySerializer(
    OrganizationQuerysetMixin,
    UniqueFieldsValidatorMixin,
    BaseOrganizationModelSerializer,
):
    name = serializers.CharField()
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.none(), allow_null=True, required=False
    )
    subcategories = serializers.SerializerMethodField()
    unique_fields = ["name"]
    organization_related_fields = {
        "parent": Category,
    }

    class Meta:
        model = Category
        fields = ("id", "name", "parent", "subcategories")

    def get_subcategories(self, obj):
        serializer = self.__class__(
            obj.subcategories.all(), many=True, context=self.context
        )
        return serializer.data


class ManufacturerSerializer(
    UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer
):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    unique_fields = ["name"]

    class Meta:
        model = Manufacturer
        fields = ("id", "name", "description")
        read_only_fields = ("id",)


class ColorSerializer(UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer):
    name = serializers.CharField()
    code = serializers.CharField(max_length=25, allow_blank=True, required=False)
    hex = serializers.CharField(max_length=7, allow_blank=True, required=False)
    unique_fields = ["name"]

    class Meta:
        model = Color
        fields = ("id", "name", "code", "hex")


class MeasurementUnitSerializer(
    UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer
):
    unique_fields = ["unit", "abbreviation"]

    class Meta:
        model = MeasurementUnit
        fields = ("id", "unit", "abbreviation", "okei_code")
