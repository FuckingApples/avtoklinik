from django_filters import rest_framework as filters

from .models import Manufacturer


class ManufacturerFilter(filters.FilterSet):
    class Meta:
        model = Manufacturer
        fields = {
            "name": ["icontains"],
            "description": ["icontains"],
        }
