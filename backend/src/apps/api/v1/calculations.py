from django.urls import path
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.api.serializers.calculations import CalculationSerializer
from apps.core.views.base import BaseOrganizationDetailView, BaseOrganizationModelView
from apps.calculations.models import Calculation


@extend_schema(tags=['Калькуляции'])
@extend_schema_view(
    post=extend_schema(
        summary="Создание калькуляции",
        request=CalculationSerializer,
        responses={status.HTTP_201_CREATED: CalculationSerializer},
    ),
    get=extend_schema(
        summary="Получение списка калькуляций",
        responses={status.HTTP_200_OK: CalculationSerializer},
    ),
)
class OrganizationCalculationsAPI(BaseOrganizationModelView):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer


@extend_schema(tags=["Калькуляции"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление калькуляции",
        request=CalculationSerializer,
        responses={status.HTTP_200_OK: CalculationSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о калькуляции",
        responses={status.HTTP_200_OK: CalculationSerializer},
    ),
    delete=extend_schema(
        summary="Удаление кальцуляции",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class CalculationAPI(BaseOrganizationDetailView):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer


urlpatterns = [
    path(
        "",
        OrganizationCalculationsAPI.as_view(),
        name="organization_calculations",
    ),
    path(
        "<int:id>/",
        CalculationAPI.as_view(),
        name="calculations",
    ),
]