from dataclasses import dataclass
from typing import TYPE_CHECKING

from rest_framework import serializers

if TYPE_CHECKING:
    from apps.cars.models import Car


@dataclass
class CarDTO:
    vin: str
    frame: str
    brand: str
    model: str
    year: int
    color: str
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
            color=car.color,
            license_plate=car.license_plate,
            license_plate_region=car.license_plate_region,
            mileage=car.mileage,
            id=car.id,
        )


class CarSerializer(serializers.Serializer):

    def to_internal_value(self, data: "Car") -> "CarDTO":
        data = super().to_internal_value(data)
        return CarDTO(**data)

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
