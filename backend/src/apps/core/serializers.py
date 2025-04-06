from rest_framework import serializers


class BaseOrganizationModelSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        organization = self.context.get("organization")
        if organization:
            validated_data["organization"] = organization
        return super().create(validated_data)
