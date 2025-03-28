from dataclasses import dataclass
from rest_framework import serializers
from apps.manufacturers.models import Manufacturer

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
        extra_kwargs = {
            'organization': {'required': True}
        }

    def validate(self, data):
        if Manufacturer.objects.filter(
            name=data['name'],
            organization=data['organization'],
            is_deleted=False
        ).exists():
            raise serializers.ValidationError(
                {
                    "message": "A manufacturer with that name already exists in this organization.",
                    "code": "manufacturer_already_exists"
                }
            )
        return data

    def to_representation(self, instance):
        if isinstance(instance, ManufacturerDTO):
            return {
                'id': instance.id,
                'name': instance.name,
                'organization_id': instance.organization_id,
                'description': instance.description,
                'is_deleted': instance.is_deleted
            }
        return super().to_representation(instance)

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        return ret
