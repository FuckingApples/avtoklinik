from rest_framework import serializers

from apps.cars.models import Car
from apps.clients.models import Client
from apps.core.mixins import UniqueFieldsValidatorMixin, OrganizationQuerysetMixin
from apps.core.serializers import BaseOrganizationModelSerializer
from apps.deals.models import Deal


class DealSerializer(
    OrganizationQuerysetMixin,
    UniqueFieldsValidatorMixin,
    BaseOrganizationModelSerializer,
):
    number = serializers.CharField()
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.none())
    car = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.none(),
        allow_null=True,
        required=False,
    )
    comment = serializers.CharField(required=False, allow_blank=True)
    unique_fields = ["number"]
    organization_related_fields = {
        "client": Client,
        "car": Car,
    }

    class Meta:
        model = Deal
        fields = ("id", "number", "client", "car", "comment")
