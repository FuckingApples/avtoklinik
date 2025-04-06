from rest_framework import serializers

from apps.api.serializers.registries import ColorSerializer
from apps.cars.models import Car
from apps.core.exceptions import DetailedValidationException
from apps.core.serializers import BaseOrganizationModelSerializer
from apps.registries.models import Color


class CarSerializer(BaseOrganizationModelSerializer):
    vin = serializers.CharField()
    frame = serializers.CharField(required=False, allow_blank=True)
    brand = serializers.CharField()
    model = serializers.CharField()
    year = serializers.IntegerField()
    color_id = serializers.PrimaryKeyRelatedField(
        queryset=Color.objects.none(), write_only=True, source="color"
    )
    color = ColorSerializer(read_only=True)
    license_plate = serializers.CharField()
    license_plate_region = serializers.CharField()
    mileage = serializers.IntegerField()

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
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        organization = self.context.get("organization")

        if organization and self.context["request"].method in ["POST", "PUT", "PATCH"]:
            self.fields["color_id"].queryset = Color.objects.filter(
                organization=organization
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
