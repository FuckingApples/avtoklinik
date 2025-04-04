from django.urls import path

from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.warehouses.models import Warehouse
from apps.api.serializers.warehouses import WarehouseSerializer


class OrganizationWarehousesAPI(BaseOrganizationModelView):
    model = Warehouse
    serializer_class = WarehouseSerializer


class WarehousesAPI(BaseOrganizationDetailView):
    model = Warehouse
    serializer_class = WarehouseSerializer
    lookup_field = "warehouse_id"


urlpatterns = [
    path(
        "",
        OrganizationWarehousesAPI.as_view(),
        name="organization_warehouses",
    ),
    path(
        "<int:warehouse_id>/",
        WarehousesAPI.as_view(),
        name="warehouses",
    ),
]
