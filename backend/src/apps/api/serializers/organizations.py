from rest_framework import serializers
from apps.organizations.models import Organization, Membership


class OrganizationSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ("id", "public_id", "name", "user_role")

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)
        super().__init__(*args, **kwargs)

        if fields:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def get_user_role(self, obj):
        user = self.context["request"].user
        membership = user.memberships.filter(organization=obj).first()
        if membership:
            return membership.role
        return None
