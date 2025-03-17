from dataclasses import dataclass

from rest_framework import serializers
from apps.workplaces.models import Workplace


@dataclass
class WorkplaceDTO:
    name: str
    color: str
    id: int = None
    icon: str = None
    description: str = None

    @classmethod
    def from_instance(cls, workplace: "Workplace") -> "WorkplaceDTO":
        return cls(
            id=workplace.id,
            icon=workplace.icon,
            name=workplace.name,
            description=workplace.description,
            color=workplace.color,
        )


class WorkplaceSerializer(serializers.ModelSerializer):
    def validate(self, data):
        organization = data.get("organization")
        name = data.get("name")
        qs = Workplace.objects.filter(organization=organization, name=name)

        if qs.exists():
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
