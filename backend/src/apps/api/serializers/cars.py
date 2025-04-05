from rest_framework import serializers

from apps.api.serializers.registries import ColorSerializer
from apps.cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    vin = serializers.CharField()
    frame = serializers.CharField(required=False, allow_blank=True)
    brand = serializers.CharField()
    model = serializers.CharField()
    year = serializers.IntegerField()
    color = ColorSerializer()
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
            "license_plate",
            "license_plate_region",
            "mileage",
        )

    def validate_mileage(self, value):
        if value < 0:
            raise serializers.ValidationError(
                {
                    "message": "Mileage cannot be negative.",
                    "code": "car_mileage_negative",
                }
            )
        return value

    def validate_plate_number(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                {
                    "message": "Plate number is too short.",
                    "code": "car_plate_too_short",
                }
            )
        return value
