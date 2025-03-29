from dataclasses import dataclass
from typing import Optional

from rest_framework import serializers

from apps.registries.models import Category


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
