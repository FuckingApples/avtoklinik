from rest_framework import serializers

from apps.core.mixins import UniqueFieldsValidatorMixin
from apps.registries.models import Category, Manufacturer, Color, MeasurementUnit


class CategorySerializer(UniqueFieldsValidatorMixin, serializers.ModelSerializer):
    name = serializers.CharField()
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.none(), allow_null=True, required=False
    )
    subcategories = serializers.SerializerMethodField()
    unique_fields = ["name"]

    class Meta:
        model = Category
        fields = ("id", "name", "parent", "subcategories")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        organization = self.context.get("organization")

        if organization:
            self.fields["parent"].queryset = Category.objects.filter(
                organization=organization
            )

    def get_subcategories(self, obj):
        serializer = self.__class__(
            obj.subcategories.all(), many=True, context=self.context
        )
        return serializer.data

    def create(self, validated_data):
        validated_data["organization"] = self.context["organization"]
        return super().create(validated_data)


class ManufacturerSerializer(UniqueFieldsValidatorMixin, serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    unique_fields = ["name"]

    class Meta:
        model = Manufacturer
        fields = ("id", "name", "organization", "description")
        read_only_fields = ("id",)


class ColorSerializer(UniqueFieldsValidatorMixin, serializers.ModelSerializer):
    name = serializers.CharField()
    code = serializers.CharField(max_length=25, allow_blank=True, required=False)
    hex = serializers.CharField(max_length=7, allow_blank=True, required=False)
    unique_fields = ["name"]

    class Meta:
        model = Color
        fields = ("id", "name", "code", "hex")

    def create(self, validated_data):
        validated_data["organization"] = self.context["organization"]
        return super().create(validated_data)


class MeasurementUnitSerializer(
    UniqueFieldsValidatorMixin, serializers.ModelSerializer
):
    unique_fields = ["unit", "abbreviation"]

    class Meta:
        model = MeasurementUnit
        fields = ("id", "unit", "abbreviation", "okei_code", "organization")
