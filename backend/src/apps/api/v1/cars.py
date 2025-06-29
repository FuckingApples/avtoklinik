from django.urls import path
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.cars.filters import CarFilter
from apps.cars.models import Car
from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.api.serializers.cars import CarSerializer


@extend_schema(tags=["Автомобили"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание автомобиля",
        request=CarSerializer,
        responses={status.HTTP_201_CREATED: CarSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех автомобилей организации",
        responses={status.HTTP_200_OK: CarSerializer},
    ),
)
class OrganizationCarsAPI(BaseOrganizationModelView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter
    ordering_fields = (
        "vin",
        "frame",
        "year",
        "mileage",
    )
    search_fields = (
        "vin",
        "frame",
        "brand",
        "model",
        "year",
        "license_plate",
    )


@extend_schema(tags=["Автомобили"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление автомобиля",
        request=CarSerializer,
        responses={status.HTTP_200_OK: CarSerializer},
    ),
    get=extend_schema(
        summary="Получение информации об автомобиле",
        responses={status.HTTP_200_OK: CarSerializer},
    ),
    delete=extend_schema(
        summary="Удаление автомобиля",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class CarsAPI(BaseOrganizationDetailView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


urlpatterns = [
    path(
        "",
        OrganizationCarsAPI.as_view(),
        name="organization_cars",
    ),
    path(
        "<int:id>/",
        CarsAPI.as_view(),
        name="cars",
    ),
]
