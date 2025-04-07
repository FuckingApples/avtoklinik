from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from apps.api.serializers.registries import ColorSerializer
from apps.cars.models import Car
from apps.core.exceptions import DetailedValidationException
from apps.core.mixins import OrganizationQuerysetMixin, UniqueFieldsValidatorMixin
from apps.core.serializers import BaseOrganizationModelSerializer
from apps.registries.models import Color


class CarSerializer(
    OrganizationQuerysetMixin,
    UniqueFieldsValidatorMixin,
    BaseOrganizationModelSerializer,
):
    color_id = serializers.PrimaryKeyRelatedField(
        queryset=Color.objects.none(), write_only=True, source="color"
    )
    color = ColorSerializer(read_only=True)
    license_plate_region = CountryField()

    organization_related_fields = {
        "color_id": Color,
    }
    unique_fields = ["vin", "frame", "license_plate"]

    class Meta:
        model = Car
        fields = (
            "id",
            "vin",
            "frame",
            "brand",
            "model",
            "year",
            "color",
            "color_id",
            "license_plate",
            "license_plate_region",
            "mileage",
            "created_at",
            "updated_at",
        )

    def validate_mileage(self, value):
        if value < 0:
            raise DetailedValidationException(
                message="Mileage cannot be negative.", code="car_mileage_negative"
            )
        return value

    def validate_license_plate(self, value):
        if len(value) < 5:
            raise DetailedValidationException(
                message="Plate number is too short.", code="car_plate_too_short"
            )
        return value
