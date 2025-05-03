from django_filters import rest_framework as filters

from .models import (
    Manufacturer,
    MeasurementUnit,
    Color,
    HourlyWage,
    Equipment,
)


class ManufacturerFilter(filters.FilterSet):
    class Meta:
        model = Manufacturer
        fields = {
            "name": ["icontains"],
            "description": ["icontains"],
        }


class MeasurementUnitFilter(filters.FilterSet):
    class Meta:
        model = MeasurementUnit
        fields = {
            "unit": ["icontains"],
            "abbreviation": ["icontains"],
            "okei_code": ["icontains"],
        }


class ColorFilter(filters.FilterSet):
    class Meta:
        model = Color
        fields = {
            "name": ["icontains"],
            "code": ["icontains"],
        }


class WorkplacesFilter(filters.FilterSet):
    class Meta:
        model = Manufacturer
        fields = {
            "name": ["icontains"],
            "description": ["icontains"],
        }


class HourlyWageFilter(filters.FilterSet):
    class Meta:
        model = HourlyWage
        fields = {
            "name": ["icontains"],
            "wage": ["icontains"],
        }


class EquipmentFilter(filters.FilterSet):
    class Meta:
        model = Equipment
        fields = {
            "name": ["icontains"],
        }
