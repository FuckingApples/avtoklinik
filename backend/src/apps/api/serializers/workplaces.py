from rest_framework import serializers
from apps.workplaces.models import Workplace


class WorkplaceSerializer(serializers.ModelSerializer):
    def validate(self, data):
        organization = data.get("organization")
        name = data.get("name")
        queryset = Workplace.objects.filter(organization=organization, name=name)

        if queryset.exists():
            raise serializers.ValidationError(
                {
                    "message": "A workplace with this name already exists.",
                    "code": "workplace_already_exists",
                }
            )
        return data

    color = serializers.RegexField(regex=r"^#(?:[0-9a-fA-F]{3}){1,2}$")

    class Meta:
        model = Workplace
        fields = ("id", "organization", "icon", "name", "description", "color")
