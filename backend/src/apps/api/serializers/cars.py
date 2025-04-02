from dataclasses import dataclass

from rest_framework import serializers

from apps.api.serializers.registries import ColorSerializer
from apps.cars.models import Car


@dataclass
class CarDTO:
    vin: str
    frame: str
    brand: str
    model: str
    year: int
    license_plate: str
    license_plate_region: str
    mileage: int
    id: int = None

    @classmethod
    def from_instance(cls, car: "Car") -> "CarDTO":
        return CarDTO(
            vin=car.vin,
            frame=car.frame,
            brand=car.brand,
            model=car.model,
            year=car.year,
            license_plate=car.license_plate,
            license_plate_region=car.license_plate_region,
            mileage=car.mileage,
            id=car.id,
        )


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
