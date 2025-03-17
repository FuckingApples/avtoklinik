from dataclasses import dataclass

from rest_framework import serializers
from apps.workplaces.models import Workplace
import re


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
                "Workplace with this name already exists."
            )
        return data

    def validate_color(self, value):
        if len(value) != 7 or not re.fullmatch(r"^#[0-9A-Fa-f]{6}$", value):
            raise serializers.ValidationError("Color must be a valid HEX format.")
        return value

    class Meta:
        model = Workplace
        fields = ("id", "organization", "icon", "name", "description", "color")
