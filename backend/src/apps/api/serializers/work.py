from rest_framework import serializers

from apps.work.models import Work
from apps.registries.models import HourlyWage
from apps.core.serializers import BaseOrganizationModelSerializer
from apps.core.mixins import (
    UniqueFieldsValidatorMixin,
    OrganizationQuerysetMixin,
)

class WorkSerializer(
    OrganizationQuerysetMixin,
    UniqueFieldsValidatorMixin,
    BaseOrganizationModelSerializer,
):
    hourly_wage = serializers.PrimaryKeyRelatedField(
        queryset=HourlyWage.objects.none(),
        allow_null=True,
        required=False
    )
    related_works = serializers.PrimaryKeyRelatedField(
        queryset=Work.objects.none(),
        many=True,
        required=False
    )

    organization_related_fields = {
        "hourly_wage": HourlyWage,
        "related_works": Work,
    }

    unique_fields = ["work_code"]

    class Meta:
        model = Work
        fields = (
            "id",
            "organization",
            "name",
            "member",
            "category",
            "price",
            "norm_time",
            "max_discount",
            "coefficient",
            "multiplicity",
            "comment",
            "barcode",
            "work_code",
            "hourly_wage",
            "related_works",
        )
