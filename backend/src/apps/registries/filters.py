from django_filters import rest_framework as filters

from .models import Manufacturer, MeasurementUnit


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
