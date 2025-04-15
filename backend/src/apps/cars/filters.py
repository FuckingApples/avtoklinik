from django_filters import rest_framework as filters

from .models import Car


class CarFilter(filters.FilterSet):
    class Meta:
        model = Car
        fields = {
            "vin": ["icontains"],
            "frame": ["icontains"],
            "brand": ["icontains"],
            "model": ["icontains"],
            "year": ["gte", "lte"],
            "color__name": ["icontains"],
            "client__last_name": ["icontains"],
            "license_plate": ["icontains"],
            "license_plate_region": ["icontains"],
            "mileage": ["gte", "lte"],
        }
