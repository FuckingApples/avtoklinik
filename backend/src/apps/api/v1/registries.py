from django.urls import path, include
from rest_framework import status
from rest_framework.response import Response

from apps.api.serializers.registries import (
    CategorySerializer,
    ManufacturerSerializer,
    ColorSerializer,
    MeasurementUnitSerializer,
)
from apps.registries.models import Category, Manufacturer, Color, MeasurementUnit
from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView


class OrganizationCategoriesAPI(BaseOrganizationModelView):
    model = Category
    serializer_class = CategorySerializer

    def get_queryset(self):
        return super().get_queryset().filter(parent__isnull=True)


class CategoriesAPI(BaseOrganizationDetailView):
    model = Category
    serializer_class = CategorySerializer
    lookup_field = "category_id"


class OrganizationColorsAPI(BaseOrganizationModelView):
    model = Color
    serializer_class = ColorSerializer


class ColorsAPI(BaseOrganizationDetailView):
    model = Color
    serializer_class = ColorSerializer
    lookup_field = "color_id"


class OrganizationMeasurementUnitsAPI(BaseOrganizationModelView):
    model = MeasurementUnit
    serializer_class = MeasurementUnitSerializer


class MeasurementUnitsAPI(BaseOrganizationDetailView):
    model = MeasurementUnit
    serializer_class = MeasurementUnitSerializer
    lookup_field = "measurement_unit_id"


class OrganizationManufacturersAPI(BaseOrganizationModelView):
    model = Manufacturer
    serializer_class = ManufacturerSerializer


class ManufacturersAPI(BaseOrganizationDetailView):
    model = Manufacturer
    serializer_class = ManufacturerSerializer
    lookup_field = "manufacturer_id"

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


categories_urls = [
    path(
        "",
        OrganizationCategoriesAPI.as_view(),
        name="organization_categories",
    ),
    path(
        "<int:category_id>/",
        CategoriesAPI.as_view(),
        name="categories",
    ),
]

colors_urls = [
    path(
        "",
        OrganizationColorsAPI.as_view(),
        name="organization_colors",
    ),
    path(
        "<int:color_id>/",
        ColorsAPI.as_view(),
        name="colors",
    ),
]

measurement_unit_urls = [
    path(
        "",
        OrganizationMeasurementUnitsAPI.as_view(),
        name="organization_measurement_units",
    ),
    path(
        "<int:measurement_unit_id>/",
        MeasurementUnitsAPI.as_view(),
        name="measurement_units",
    ),
]

manufacturers_urls = [
    path(
        "",
        OrganizationManufacturersAPI.as_view(),
        name="organization_manufacturers",
    ),
    path(
        "<int:manufacturer_id>/",
        ManufacturersAPI.as_view(),
        name="manufacturers",
    ),
]

urlpatterns = [
    path("categories/", include(categories_urls)),
    path("manufacturers/", include(manufacturers_urls)),
    path("colors/", include(colors_urls)),
    path("measurement_units/", include(measurement_unit_urls)),
]
