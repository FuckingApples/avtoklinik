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
    permission_classes = [IsAuthenticated]
    model = Category
    serializer_class = CategorySerializer
    lookup_field = "category_id"


class OrganizationColorsAPI(views.APIView):
    def get(self, request, organization_id):
        organization = get_object_or_404(Organization, id=organization_id)
        colors = Color.objects.filter(organization=organization)
        serializer = ColorSerializer(colors, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, organization_id):
        organization = get_object_or_404(Organization, id=organization_id)
        serializer = ColorSerializer(
            data=request.data,
            context={"organization": organization, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ColorsAPI(views.APIView):
    def get(self, request, organization_id, color_id):
        organization = get_object_or_404(Organization, id=organization_id)
        color = Color.objects.filter(organization=organization, id=color_id).first()

        if not color:
            return Response(
                {"message": "Color not found.", "code": "color_not_found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ColorSerializer(color)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, organization_id, color_id):
        organization = get_object_or_404(Organization, id=organization_id)
        color = get_object_or_404(Color, id=color_id, organization=organization)
        serializer = ColorSerializer(
            color,
            data=request.data,
            partial=True,
            context={"organization": organization, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, organization_id, color_id):
        organization = get_object_or_404(Organization, id=organization_id)
        color = get_object_or_404(Color, id=color_id, organization=organization)
        color.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class OrganizationMeasurementUnitsAPI(views.APIView):
    def get(self, request, organization_id):
        organization = get_object_or_404(Organization, id=organization_id)
        measurement_units = MeasurementUnit.objects.filter(organization=organization)
        serializer = MeasurementUnitSerializer(measurement_units, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, organization_id):
        organization = get_object_or_404(Organization, id=organization_id)
        serializer = MeasurementUnitSerializer(
            data=request.data,
            context={"organization": organization, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MeasurementUnitsAPI(views.APIView):
    def get(self, request, organization_id, measurement_unit_id):
        organization = get_object_or_404(Organization, id=organization_id)
        measurement_unit = MeasurementUnit.objects.filter(
            organization=organization, id=measurement_unit_id
        ).first()

        if not measurement_unit:
            return Response(
                {
                    "message": "Measurement unit not found.",
                    "code": "measurement_unit_not_found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MeasurementUnitSerializer(measurement_unit)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, organization_id, measurement_unit_id):
        organization = get_object_or_404(Organization, id=organization_id)
        measurement_unit = get_object_or_404(
            MeasurementUnit, id=measurement_unit_id, organization=organization
        )
        serializer = MeasurementUnitSerializer(
            measurement_unit,
            data=request.data,
            partial=True,
            context={"organization": organization, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, organization_id, measurement_unit_id):
        organization = get_object_or_404(Organization, id=organization_id)
        measurement_unit = get_object_or_404(
            MeasurementUnit, id=measurement_unit_id, organization=organization
        )
        measurement_unit.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


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
