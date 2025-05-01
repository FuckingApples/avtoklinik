from dataclasses import dataclass
from typing import Optional

from rest_framework import serializers


@dataclass
class TemplateDTO:
    is_organization: bool
    text: str
    field_id: str
    id: Optional[int] = None


class TemplateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_organization = serializers.BooleanField()
    text = serializers.CharField()
    field_id = serializers.CharField()

    def to_internal_value(self, data) -> TemplateDTO:
        validated = super().to_internal_value(data)
        return TemplateDTO(**validated)
