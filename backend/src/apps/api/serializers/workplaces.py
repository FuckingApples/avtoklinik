from rest_framework import serializers

from apps.core.mixins import UniqueFieldsValidatorMixin
from apps.core.serializers import BaseOrganizationModelSerializer
from apps.workplaces.models import Workplace


class WorkplaceSerializer(UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer):
    unique_fields = ["name"]

    color = serializers.RegexField(regex=r"^#(?:[0-9a-fA-F]{3}){1,2}$")

    class Meta:
        model = Workplace
        fields = ("id", "icon", "name", "description", "color")
