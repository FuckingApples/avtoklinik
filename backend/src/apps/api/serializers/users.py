from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

from apps.api.serializers.organizations import OrganizationSerializer, OrganizationDTO

if TYPE_CHECKING:
    from apps.users.models import User


@dataclass
class UserDTO:
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    avatar: Optional[str] = None
    password: Optional[str] = None
    is_email_verified: Optional[bool] = None
    organizations: Optional[List[OrganizationDTO]] = None
    id: Optional[int] = None

    @classmethod
    def from_instance(cls, user: "User") -> "UserDTO":
        organizations = []
        if hasattr(user, "organizations"):
            organizations_queryset = user.organizations.all()
            for org in organizations_queryset:
                org_dto = OrganizationDTO.from_instance(org)
                organizations.append(org_dto)

        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            is_email_verified=user.is_email_verified,
            organizations=organizations,
            id=user.id,
        )


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    avatar = serializers.URLField(required=False)
    password = serializers.CharField(write_only=True)
    is_email_verified = serializers.BooleanField(read_only=True)
    organizations = serializers.SerializerMethodField(read_only=True)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)

        # Обновляем остальные поля
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    @extend_schema_field(OrganizationSerializer)
    def get_organizations(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return []

        organizations = obj.organizations.all()
        return OrganizationSerializer(
            organizations, many=True, context={"request": request}
        ).data
