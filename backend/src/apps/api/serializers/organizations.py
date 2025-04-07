from rest_framework import serializers
from apps.organizations.models import Organization, Membership


class OrganizationSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ("id", "public_id", "name", "user_role")

    def get_user_role(self, obj):
        user = self.context["request"].user
        membership = Membership.objects.filter(user=user, organization=obj).first()
        if membership:
            return membership.role
        return None
