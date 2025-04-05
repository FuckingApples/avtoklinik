from django.urls import path, include
from drf_spectacular.utils import extend_schema, extend_schema_view
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


@extend_schema(tags=["Списки"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание категории",
        request=CategorySerializer,
        responses={status.HTTP_201_CREATED: CategorySerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех категорий организации",
        responses={status.HTTP_200_OK: CategorySerializer},
    ),
)
class OrganizationCategoriesAPI(BaseOrganizationModelView):
    model = Category
    serializer_class = CategorySerializer

    def get_queryset(self):
        return super().get_queryset().filter(parent__isnull=True)


@extend_schema(tags=["Списки"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление категории",
        request=CategorySerializer,
        responses={status.HTTP_200_OK: CategorySerializer},
    ),
    get=extend_schema(
        summary="Получение информации о категории",
        responses={status.HTTP_200_OK: CategorySerializer},
    ),
    delete=extend_schema(
        summary="Удаление категории",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class CategoriesAPI(BaseOrganizationDetailView):
    model = Category
    serializer_class = CategorySerializer
    lookup_field = "category_id"


@extend_schema(tags=["Списки"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание цвета",
        request=ColorSerializer,
        responses={status.HTTP_201_CREATED: ColorSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех цветов организации",
        responses={status.HTTP_200_OK: ColorSerializer},
    ),
)
class OrganizationColorsAPI(BaseOrganizationModelView):
    model = Color
    serializer_class = ColorSerializer


@extend_schema(tags=["Списки"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление цвета",
        request=ColorSerializer,
        responses={status.HTTP_200_OK: ColorSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о цвете",
        responses={status.HTTP_200_OK: ColorSerializer},
    ),
    delete=extend_schema(
        summary="Удаление цвета",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class ColorsAPI(BaseOrganizationDetailView):
    model = Color
    serializer_class = ColorSerializer
    lookup_field = "color_id"


@extend_schema(tags=["Списки"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание единицы измерения",
        request=MeasurementUnitSerializer,
        responses={status.HTTP_201_CREATED: MeasurementUnitSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех единиц измерения организации",
        responses={status.HTTP_200_OK: MeasurementUnitSerializer},
    ),
)
class OrganizationMeasurementUnitsAPI(BaseOrganizationModelView):
    model = MeasurementUnit
    serializer_class = MeasurementUnitSerializer


@extend_schema(tags=["Списки"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление единицы измерения",
        request=MeasurementUnitSerializer,
        responses={status.HTTP_200_OK: MeasurementUnitSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о единице измерения",
        responses={status.HTTP_200_OK: MeasurementUnitSerializer},
    ),
    delete=extend_schema(
        summary="Удаление единицы измерения",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class MeasurementUnitsAPI(BaseOrganizationDetailView):
    model = MeasurementUnit
    serializer_class = MeasurementUnitSerializer
    lookup_field = "measurement_unit_id"


@extend_schema(tags=["Списки"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание производителя",
        request=ManufacturerSerializer,
        responses={status.HTTP_201_CREATED: ManufacturerSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех производителей организации",
        responses={status.HTTP_200_OK: ManufacturerSerializer},
    ),
)
class OrganizationManufacturersAPI(BaseOrganizationModelView):
    model = Manufacturer
    serializer_class = ManufacturerSerializer


@extend_schema(tags=["Списки"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление производителя",
        request=ColorSerializer,
        responses={status.HTTP_200_OK: ColorSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о производителе",
        responses={status.HTTP_200_OK: ColorSerializer},
    ),
    delete=extend_schema(
        summary="Удаление производителя",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
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
