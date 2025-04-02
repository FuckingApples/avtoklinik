from dataclasses import dataclass
from typing import Optional

from rest_framework import serializers
from apps.registries.models import Category, Manufacturer, Color, MeasurementUnit


@dataclass
class CategoryDTO:
    name: Optional[str]
    organization: Optional[int]
    parent: Optional[int] = None
    id: Optional[int] = None

    @classmethod
    def from_instance(cls, category: "Category") -> "CategoryDTO":
        return CategoryDTO(
            name=category.name,
            parent=category.parent.id if category.parent else None,
            organization=category.organization.id,
            id=category.id,
        )


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.none(), allow_null=True, required=False
    )
    subcategories = serializers.SerializerMethodField()

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

    def validate_name(self, value):
        organization = self.context.get("organization")
        queryset = Category.objects.filter(organization=organization, name=value)

        if queryset.exists():
            raise serializers.ValidationError(
                {
                    "message": "A category with this name already exists.",
                    "code": "category_already_exists",
                }
            )

        return value

    def create(self, validated_data):
        validated_data["organization"] = self.context["organization"]
        return super().create(validated_data)


@dataclass
class ManufacturerDTO:
    name: str
    organization_id: int
    id: int = None
    description: str = None
    is_deleted: bool = False

    @classmethod
    def from_instance(cls, manufacturer: "Manufacturer") -> "ManufacturerDTO":
        return cls(
            id=manufacturer.id,
            name=manufacturer.name,
            organization_id=manufacturer.organization_id,
            description=manufacturer.description,
            is_deleted=manufacturer.is_deleted,
        )


class ManufacturerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Manufacturer
        fields = ("id", "name", "organization", "description", "is_deleted")
        read_only_fields = ("id", "is_deleted")

    def validate(self, data):
        if Manufacturer.objects.filter(
            name=data["name"], organization=data["organization"]
        ).exists():
            raise serializers.ValidationError(
                {
                    "message": "A manufacturer with that name already exists in this organization.",
                    "code": "manufacturer_already_exists",
                }
            )
        return data

    def to_representation(self, instance):
        if isinstance(instance, ManufacturerDTO):
            return {
                "id": instance.id,
                "name": instance.name,
                "organization_id": instance.organization_id,
                "description": instance.description,
                "is_deleted": instance.is_deleted,
            }
        return super().to_representation(instance)


class ColorSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    code = serializers.CharField(max_length=25, allow_blank=True, required=False)
    hex = serializers.CharField(max_length=7, allow_blank=True, required=False)

    class Meta:
        model = Color
        fields = ("id", "name", "code", "hex")

    def create(self, validated_data):
        validated_data["organization"] = self.context["organization"]
        return super().create(validated_data)


class MeasurementUnitSerializer(serializers.ModelSerializer):
    def validate(self, data):
        organization = data.get("organization")
        unit = data.get("unit")
        abbreviation = data.get("abbreviation")
        queryset = MeasurementUnit.objects.filter(
            organization=organization, unit=unit, abbreviation=abbreviation
        )

        if queryset.exists():
            raise serializers.ValidationError(
                {
                    "message": "A measurement unit with this name or abbreviation already exists.",
                    "code": "measurement_unit_already_exists",
                }
            )
        return data

    class Meta:
        model = MeasurementUnit
        fields = ("id", "unit", "abbreviation", "okei_code", "organization")
