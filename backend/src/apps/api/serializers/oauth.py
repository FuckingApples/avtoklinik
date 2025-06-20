from dataclasses import dataclass

from rest_framework import serializers

from apps.oauth.models import OAuthProvider


class OAuthProviderSerializer(serializers.ModelSerializer):
    provider_display = serializers.CharField(
        source="get_provider_display", read_only=True
    )

    class Meta:
        model = OAuthProvider
        fields = (
            "id",
            "provider",
            "provider_display",
            "uid",
            "created_at",
            "updated_at",
        )


class OAuthSerializer(serializers.Serializer):
    code = serializers.CharField(write_only=True)
    code_verifier = serializers.CharField(write_only=True)


class VKOAuthSerializer(OAuthSerializer):
    device_id = serializers.CharField(write_only=True)
    redirect_uri = serializers.CharField(write_only=True)
