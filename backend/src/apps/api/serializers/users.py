from rest_framework import serializers
from dataclasses import dataclass
from typing import TYPE_CHECKING

from apps.api.serializers.organizations import OrganizationSerializer

if TYPE_CHECKING:
    from apps.users.models import User


@dataclass
class RegisterUserDTO:
    first_name: str
    last_name: str
    email: str
    password: str = None
    id: int = None

    @classmethod
    def from_instance(cls, user: "User") -> "RegisterUserDTO":
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            id=user.id,
        )


class RegisterUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def to_internal_value(self, data: "User") -> "RegisterUserDTO":
        data = super().to_internal_value(data)

        return RegisterUserDTO(**data)


class UserInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    is_email_verified = serializers.BooleanField(read_only=True)
    organizations = OrganizationSerializer(many=True, read_only=True)
