from django.urls import path
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.warehouses.models import Warehouse
from apps.api.serializers.warehouses import WarehouseSerializer


@extend_schema(tags=["Склады"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание склада",
        request=WarehouseSerializer,
        responses={status.HTTP_201_CREATED: WarehouseSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех складов организации",
        responses={status.HTTP_200_OK: WarehouseSerializer},
    ),
)
class OrganizationWarehousesAPI(BaseOrganizationModelView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


@extend_schema(tags=["Склады"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление склада",
        request=WarehouseSerializer,
        responses={status.HTTP_200_OK: WarehouseSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о складе",
        responses={status.HTTP_200_OK: WarehouseSerializer},
    ),
    delete=extend_schema(
        summary="Удаление склада",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class WarehousesAPI(BaseOrganizationDetailView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


urlpatterns = [
    path(
        "",
        OrganizationWarehousesAPI.as_view(),
        name="organization_warehouses",
    ),
    path(
        "<int:id>/",
        WarehousesAPI.as_view(),
        name="warehouses",
    ),
]
