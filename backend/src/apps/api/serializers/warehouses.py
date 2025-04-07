from rest_framework import serializers

from apps.core.mixins import UniqueFieldsValidatorMixin, OrganizationQuerysetMixin
from apps.core.serializers import BaseOrganizationModelSerializer
from apps.documents.models import Product
from apps.warehouses.models import Warehouse, ProductStock


class WarehouseSerializer(UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer):
    unique_fields = ["name"]

    class Meta:
        model = Warehouse
        fields = ("id", "name", "comment", "is_trade")


class ProductStockSerializer(
    OrganizationQuerysetMixin,
    UniqueFieldsValidatorMixin,
    BaseOrganizationModelSerializer,
):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    warehouse = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all())
    quantity = serializers.IntegerField(default=0, required=False)
    unique_fields = ["warehouse", "product"]
    organization_related_fields = {
        "product": Product,
        "warehouse": Warehouse,
    }

    class Meta:
        model = ProductStock
        fields = ("id", "warehouse", "product", "quantity")
