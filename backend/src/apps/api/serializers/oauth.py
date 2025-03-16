from rest_framework import serializers
from dataclasses import dataclass

from apps.oauth.models import OAuthProvider


class OAuthProviderSerializer(serializers.ModelSerializer):
    provider_display = serializers.CharField(
        source="get_provider_display", read_only=True
    )

    class Meta:
        model = OAuthProvider
        fields = ["id", "provider", "provider_display", "uid", "created_at"]


@dataclass
class YandexOAuthDTO:
    code: str

    @classmethod
    def from_instance(cls, code: str) -> "YandexOAuthDTO":
        return cls(code=code)


class YandexOAuthSerializer(serializers.Serializer):
    code = serializers.CharField(write_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return YandexOAuthDTO(**data)
