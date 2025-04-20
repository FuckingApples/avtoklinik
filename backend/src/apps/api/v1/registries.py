from django.urls import path, include
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.api.serializers.registries import (
    CategorySerializer,
    ManufacturerSerializer,
    ColorSerializer,
    MeasurementUnitSerializer,
    WorkplaceSerializer,
    HourlyWageSerializer,
)
from apps.registries.models import (
    Category,
    Manufacturer,
    Color,
    MeasurementUnit,
    Workplace,
    HourlyWage,
)
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
    queryset = Category.objects.all()
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
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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
    queryset = Color.objects.all()
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
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


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
    queryset = MeasurementUnit.objects.all()
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
    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer


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
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


@extend_schema(tags=["Списки"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление производителя",
        request=ManufacturerSerializer,
        responses={status.HTTP_200_OK: ManufacturerSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о производителе",
        responses={status.HTTP_200_OK: ManufacturerSerializer},
    ),
    delete=extend_schema(
        summary="Удаление производителя",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class ManufacturersAPI(BaseOrganizationDetailView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


@extend_schema(tags=["Рабочие места"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание рабочего места",
        request=WorkplaceSerializer,
        responses={status.HTTP_201_CREATED: WorkplaceSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех рабочих мест организации",
        responses={status.HTTP_200_OK: WorkplaceSerializer},
    ),
)
class OrganizationWorkplacesAPI(BaseOrganizationModelView):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


@extend_schema(tags=["Рабочие места"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление рабочего места",
        request=WorkplaceSerializer,
        responses={status.HTTP_200_OK: WorkplaceSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о рабочем месте",
        responses={status.HTTP_200_OK: WorkplaceSerializer},
    ),
    delete=extend_schema(
        summary="Удаление рабочего места",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class WorkplacesAPI(BaseOrganizationDetailView):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


@extend_schema(tags=["Нормо-часы"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание нормо-часа",
        request=HourlyWageSerializer,
        responses={status.HTTP_201_CREATED: HourlyWageSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех нормо-часов организации",
        responses={status.HTTP_200_OK: HourlyWageSerializer(many=True)},
    ),
)
class OrganizationHourlyWagesAPI(BaseOrganizationModelView):
    queryset = HourlyWage.objects.all()
    serializer_class = HourlyWageSerializer


@extend_schema(tags=["Нормо-часы"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление нормо-часа",
        request=HourlyWageSerializer,
        responses={status.HTTP_200_OK: HourlyWageSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о нормо-часе",
        responses={status.HTTP_200_OK: HourlyWageSerializer},
    ),
    delete=extend_schema(
        summary="Удаление нормо-часа",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class HourlyWagesAPI(BaseOrganizationDetailView):
    queryset = HourlyWage.objects.all()
    serializer_class = HourlyWageSerializer


categories_urls = [
    path(
        "",
        OrganizationCategoriesAPI.as_view(),
        name="organization_categories",
    ),
    path(
        "<int:id>/",
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
        "<int:id>/",
        ColorsAPI.as_view(),
        name="colors",
    ),
]

measurement_units_urls = [
    path(
        "",
        OrganizationMeasurementUnitsAPI.as_view(),
        name="organization_measurement_units",
    ),
    path(
        "<int:id>/",
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
        "<int:id>/",
        ManufacturersAPI.as_view(),
        name="manufacturers",
    ),
]

workplaces_urls = [
    path(
        "",
        OrganizationWorkplacesAPI.as_view(),
        name="organization_workplaces",
    ),
    path(
        "<int:id>/",
        WorkplacesAPI.as_view(),
        name="workplaces",
    ),
]

hourly_wages_urls = [
    path(
        "",
        OrganizationHourlyWagesAPI.as_view(),
        name="organization_hourly_wages",
    ),
    path(
        "<int:id>/",
        HourlyWagesAPI.as_view(),
        name="hourly_wages",
    ),
]

urlpatterns = [
    path("categories/", include(categories_urls)),
    path("manufacturers/", include(manufacturers_urls)),
    path("colors/", include(colors_urls)),
    path("measurement_units/", include(measurement_units_urls)),
    path("workplaces/", include(workplaces_urls)),
    path("hourly_wages/", include(hourly_wages_urls)),
]
