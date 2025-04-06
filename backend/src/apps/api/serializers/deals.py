from rest_framework import serializers

from apps.cars.models import Car
from apps.clients.models import Client
from apps.core.mixins import UniqueFieldsValidatorMixin
from apps.core.serializers import BaseOrganizationModelSerializer
from apps.deals.models import Deal


class DealSerializer(UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer):
    number = serializers.CharField()
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.none())
    car = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.none(),
        allow_null=True,
        required=False,
    )
    comment = serializers.CharField(required=False, allow_blank=True)
    unique_fields = ["number"]

    class Meta:
        model = Deal
        fields = ("id", "number", "client", "car", "comment")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        organization = self.context.get("organization")

        if organization and self.context["request"].method in ["POST", "PUT", "PATCH"]:
            self.fields["client"].queryset = Client.objects.filter(
                organization=organization
            )
            self.fields["car"].queryset = Car.objects.filter(organization=organization)
