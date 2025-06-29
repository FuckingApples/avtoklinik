from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from apps.api.serializers.organizations import OrganizationSerializer


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
            organizations,
            many=True,
            context={"request": request},
            fields=["id", "public_id", "name", "user_role"],
        ).data
