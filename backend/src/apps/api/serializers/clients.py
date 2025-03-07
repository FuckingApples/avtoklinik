from dataclasses import dataclass
from typing import TYPE_CHECKING

from rest_framework import serializers

if TYPE_CHECKING:
    from apps.clients.models import Client


@dataclass
class ClientDTO:
    first_name: str
    last_name: str
    phone: str
    middle_name: str = None
    email: str = None

    @classmethod
    def from_instance(cls, client: "Client") -> "ClientDTO":
        return cls(
            first_name=client.first_name,
            last_name=client.last_name,
            phone=client.phone,
            middle_name=client.middle_name,
            email=client.email,
        )


class ClientSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.RegexField(regex=r"^(\+7|8)\d{10}$")
    email = serializers.EmailField(required=False, allow_blank=True)

    def to_internal_value(self, data: "Client") -> "ClientDTO":
        data = super().to_internal_value(data)

        return ClientDTO(**data)
