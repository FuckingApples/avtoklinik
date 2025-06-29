from rest_framework import serializers

from apps.deals.models import Deal, ClientRequest
from apps.cars.models import Car
from apps.clients.models import Client
from apps.registries.models import Workplace

from apps.core.mixins import (
    UniqueFieldsValidatorMixin,
    OrganizationQuerysetMixin,
    AutoCreateRelatedModelMixin,
)
from apps.core.serializers import BaseOrganizationModelSerializer


class DealSerializer(
    OrganizationQuerysetMixin,
    UniqueFieldsValidatorMixin,
    BaseOrganizationModelSerializer,
):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.none())
    car = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.none(),
        allow_null=True,
        required=False,
    )

    organization_related_fields = {
        "client": Client,
        "car": Car,
    }
    unique_fields = ["number"]

    class Meta:
        model = Deal
        fields = (
            "id",
            "number",
            "client",
            "car",
            "comment",
            "created_at",
            "updated_at",
        )


class ClientRequestSerializer(
    AutoCreateRelatedModelMixin,
    UniqueFieldsValidatorMixin,
    OrganizationQuerysetMixin,
    BaseOrganizationModelSerializer,
):
    deal = serializers.PrimaryKeyRelatedField(
        queryset=Deal.objects.none(), allow_null=True, required=False
    )
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.none())
    workplace = serializers.PrimaryKeyRelatedField(
        queryset=Workplace.objects.none(), allow_null=True, required=True
    )

    creation_field_name = "deal"
    creation_model = Deal
    creation_required_fields = ["client"]

    organization_related_fields = {
        "deal": Deal,
        "client": Client,
        "workplace": Workplace,
    }
    unique_fields = ["number"]

    class Meta:
        model = ClientRequest
        fields = (
            "id",
            "number",
            "organization",
            "deal",
            "employee",
            "client",
            "workplace",
            "date_start",
            "date_end",
            "comment",
            "created_at",
            "updated_at",
        )
