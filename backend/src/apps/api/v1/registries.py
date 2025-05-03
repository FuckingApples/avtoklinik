from django.urls import path, include
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.serializers.registries import (
    CategorySerializer,
    ManufacturerSerializer,
    ColorSerializer,
    MeasurementUnitSerializer,
    WorkplaceSerializer,
    HourlyWageSerializer,
    EquipmentSerializer,
)
from apps.registries.filters import (
    ManufacturerFilter,
    MeasurementUnitFilter,
    WorkplacesFilter,
    HourlyWageFilter,
    EquipmentFilter,
)
from apps.registries.models import (
    Category,
    Manufacturer,
    Color,
    MeasurementUnit,
    Workplace,
    HourlyWage,
    Equipment,
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
    ordering_fields = (
        "name",
        "code",
    )
    search_fields = (
        "name",
        "code",
    )


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
    filterset_class = MeasurementUnitFilter
    ordering_fields = (
        "unit",
        "abbreviation",
        "okei_code",
    )
    search_fields = (
        "unit",
        "abbreviation",
        "okei_code",
    )


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
    filterset_class = ManufacturerFilter
    ordering_fields = ("name",)
    search_fields = (
        "name",
        "description",
    )


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


@extend_schema(tags=["Списки"])
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
    filterset_class = WorkplacesFilter
    ordering_fields = (
        "name",
        "description",
    )
    search_fields = (
        "name",
        "description",
    )


@extend_schema(tags=["Списки"])
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


@extend_schema(tags=["Списки"])
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
    filterset_class = HourlyWageFilter
    ordering_fields = (
        "name",
        "wage",
    )
    search_fields = (
        "name",
        "wage",
    )


@extend_schema(tags=["Списки"])
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


@extend_schema(tags=["Списки"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание комплектности",
        request=EquipmentSerializer,
        responses={status.HTTP_201_CREATED: EquipmentSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех комплектностей организации",
        responses={status.HTTP_200_OK: EquipmentSerializer(many=True)},
    ),
)
class OrganizationEquipmentsAPI(BaseOrganizationModelView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filterset_class = EquipmentFilter
    ordering_fields = ("name",)
    search_fields = ("name",)


@extend_schema(tags=["Списки"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление комплектности",
        request=EquipmentSerializer,
        responses={status.HTTP_200_OK: EquipmentSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о комплектности",
        responses={status.HTTP_200_OK: EquipmentSerializer},
    ),
    delete=extend_schema(
        summary="Удаление комплектности",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class EquipmentsAPI(BaseOrganizationDetailView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


@extend_schema(tags=["Списки"])
@extend_schema_view(
    get=extend_schema(
        summary="Получение количества объектов справочников по организации",
        responses={status.HTTP_200_OK: OpenApiTypes.OBJECT},
    ),
)
class RegistriesCountAPI(APIView):
    def get(self, request, organization_id):
        data = {
            "categories": Category.objects.filter(
                organization_id=organization_id, parent__isnull=True
            ).count(),
            "manufacturers": Manufacturer.objects.filter(
                organization_id=organization_id
            ).count(),
            "colors": Color.objects.filter(organization_id=organization_id).count(),
            "measurement-units": MeasurementUnit.objects.filter(
                organization_id=organization_id
            ).count(),
            "workplaces": Workplace.objects.filter(
                organization_id=organization_id
            ).count(),
            "hourly-wages": HourlyWage.objects.filter(
                organization_id=organization_id
            ).count(),
            "equipments": Equipment.objects.filter(
                organization_id=organization_id
            ).count(),
        }

        return Response(data)


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

equipments_urls = [
    path(
        "",
        OrganizationEquipmentsAPI.as_view(),
        name="organization_equipments",
    ),
    path(
        "<int:id>/",
        EquipmentsAPI.as_view(),
        name="equipments",
    ),
]

registries_counts_urls = [
    path(
        "",
        RegistriesCountAPI.as_view(),
        name="registries_counts",
    )
]

urlpatterns = [
    path("categories/", include(categories_urls)),
    path("manufacturers/", include(manufacturers_urls)),
    path("colors/", include(colors_urls)),
    path("measurement_units/", include(measurement_units_urls)),
    path("workplaces/", include(workplaces_urls)),
    path("hourly_wages/", include(hourly_wages_urls)),
    path("equipments/", include(equipments_urls)),
    path("counts/", include(registries_counts_urls)),
]
