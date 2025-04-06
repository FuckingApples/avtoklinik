from rest_framework import serializers
from apps.clients.models import Client
from apps.core.serializers import BaseOrganizationModelSerializer


class ClientSerializer(BaseOrganizationModelSerializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.RegexField(regex=r"^(\+7|8)\d{10}$")
    email = serializers.EmailField(required=False, allow_blank=True)

    class Meta:
        model = Client
        fields = ("id", "first_name", "last_name", "middle_name", "phone", "email")
