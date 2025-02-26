import uuid
from dataclasses import dataclass
from typing import TYPE_CHECKING

from rest_framework import serializers

if TYPE_CHECKING:
    from apps.organizations.models import Organization


@dataclass
class OrganizationDTO:
    name: str
    public_id: uuid.UUID = None
    id: int = None

    @classmethod
    def from_instance(cls, organization: "Organization") -> "OrganizationDTO":
        return cls(
            name=organization.name,
            id=organization.id,
            public_id=organization.public_id,
        )


class OrganizationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    public_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return OrganizationDTO(**data)
