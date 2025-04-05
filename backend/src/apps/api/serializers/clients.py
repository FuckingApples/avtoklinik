from rest_framework import serializers
from apps.clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.RegexField(regex=r"^(\+7|8)\d{10}$")
    email = serializers.EmailField(required=False, allow_blank=True)

    class Meta:
        model = Client
        fields = ("id", "first_name", "last_name", "middle_name", "phone", "email")

    def create(self, validated_data):
        validated_data["organization"] = self.context["organization"]
        return super().create(validated_data)
