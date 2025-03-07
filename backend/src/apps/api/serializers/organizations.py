import uuid
from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from rest_framework import serializers
from apps.organizations.models import Membership

if TYPE_CHECKING:
    from apps.organizations.models import Organization
    from apps.users.models import User


@dataclass
class OrganizationDTO:
    name: str
    public_id: uuid.UUID = None
    id: int = None
    user_role: Optional[str] = None

    @classmethod
    def from_instance(
        cls, organization: "Organization", user: "User" = None
    ) -> "OrganizationDTO":
        return cls(
            name=organization.name,
            id=organization.id,
            public_id=organization.public_id,
            user_role=organization.get_user_role(user) if user else None,
        )


class OrganizationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    public_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    user_role = serializers.SerializerMethodField()

    def get_user_role(self, obj) -> Optional[str]:
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return None

        membership = (
            Membership.objects.filter(user=request.user, organization=obj)
            .select_related("role")
            .first()
        )

        return membership.role.name if membership and membership.role else None

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return OrganizationDTO(**data)
