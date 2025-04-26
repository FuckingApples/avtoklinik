from rest_framework import serializers


class BaseOrganizationModelSerializer(serializers.ModelSerializer):
    fields_to_delete = []

    def create(self, validated_data):
        for field in self.fields_to_delete:
            validated_data.pop(field, None)

        organization = self.context.get("organization")
        if organization:
            validated_data["organization"] = organization
        return super().create(validated_data)


class OrgPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        qs = super().get_queryset()
        org = self.context.get("organization")
        if org is not None and hasattr(qs, "filter"):
            return qs.filter(organization=org)
        return qs
