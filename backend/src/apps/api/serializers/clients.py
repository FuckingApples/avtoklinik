from rest_framework import serializers
from apps.clients.models import Client
from apps.core.serializers import BaseOrganizationModelSerializer


class ClientSerializer(BaseOrganizationModelSerializer):
    phone = serializers.RegexField(regex=r"^(\+7|8)\d{10}$")

    class Meta:
        model = Client
        fields = (
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "phone",
            "email",
            "created_at",
            "updated_at",
        )
