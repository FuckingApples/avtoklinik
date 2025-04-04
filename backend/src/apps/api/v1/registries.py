from django.urls import path, include
from rest_framework import views, status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.api.serializers.registries import (
    CategorySerializer,
    ManufacturerSerializer,
    ColorSerializer,
    MeasurementUnitSerializer,
)
from apps.organizations.models import Organization
from apps.registries.models import Category, Manufacturer, Color, MeasurementUnit
from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView


class OrganizationCategoriesAPI(BaseOrganizationModelView):
    permission_classes = [IsAuthenticated]
    model = Category
    serializer_class = CategorySerializer

    def get_queryset(self):
        return super().get_queryset().filter(parent__isnull=True)


class CategoriesAPI(BaseOrganizationDetailView):
    permission_classes = (IsAuthenticated,)
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


class ManufacturerBaseView:
    permission_classes = [IsAuthenticated]

    def get_organization(self):
        org = get_object_or_404(
            Organization.all_objects, pk=self.kwargs["organization_id"]
        )
        return org


class ManufacturerListView(ManufacturerBaseView, generics.ListAPIView):
    serializer_class = ManufacturerSerializer

    def get_queryset(self):
        return Manufacturer.objects.filter(organization=self.get_organization())


class ManufacturerCreateView(ManufacturerBaseView, generics.CreateAPIView):
    serializer_class = ManufacturerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organization=self.get_organization())
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ManufacturerDetailView(ManufacturerBaseView, generics.RetrieveAPIView):
    serializer_class = ManufacturerSerializer
    lookup_url_kwarg = "manufacturer_id"

    def get_queryset(self):
        return Manufacturer.objects.filter(organization=self.get_organization())


class ManufacturerUpdateView(ManufacturerBaseView, generics.UpdateAPIView):
    serializer_class = ManufacturerSerializer
    lookup_url_kwarg = "manufacturer_id"

    def get_queryset(self):
        return Manufacturer.objects.filter(organization=self.get_organization())


class ManufacturerDeleteView(ManufacturerBaseView, generics.DestroyAPIView):
    lookup_url_kwarg = "manufacturer_id"

    def get_queryset(self):
        return Manufacturer.objects.filter(organization=self.get_organization())

    def perform_destroy(self, instance):
        instance.soft_delete()


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
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "<int:manufacturer_id>/",
        ManufacturerDetailView.as_view(),
        name="manufacturer-detail",
    ),
    path(
        "<int:manufacturer_id>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "<int:manufacturer_id>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete",
    ),
]

urlpatterns = [
    path("categories/", include(categories_urls)),
    path("manufacturer/", include(manufacturers_urls)),
    path("colors/", include(colors_urls)),
    path("measurement_units/", include(measurement_unit_urls)),
]
