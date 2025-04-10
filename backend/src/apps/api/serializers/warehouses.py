from rest_framework import serializers

from django_countries.serializer_fields import CountryField
from apps.core.mixins import UniqueFieldsValidatorMixin, OrganizationQuerysetMixin
from apps.core.serializers import BaseOrganizationModelSerializer
from apps.warehouses.models import Warehouse, Product, ProductStock


class WarehouseSerializer(UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer):
    unique_fields = ["name"]

    class Meta:
        model = Warehouse
        fields = ("id", "name", "comment", "is_trade", "created_at", "updated_at")


class ProductSerializer(BaseOrganizationModelSerializer):
    country = CountryField(required=False, allow_null=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "receipt_name",
            "article",
            "barcode",
            "quantity",
            "cost_price",
            "selling_price",
            "max_discount",
            "critical_stock",
            "desired_stock",
            "net_mass",
            "gross_mass",
            "country",
            "comment",
            "category",
            "sales_unit",
            "write_off_unit",
            "manufacturer",
            "created_at",
            "updated_at",
        )


class ProductStockSerializer(
    OrganizationQuerysetMixin,
    UniqueFieldsValidatorMixin,
    BaseOrganizationModelSerializer,
):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    warehouse = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all())

    organization_related_fields = {
        "product": Product,
        "warehouse": Warehouse,
    }
    unique_fields = ["warehouse", "product"]

    class Meta:
        model = ProductStock
        fields = ("id", "warehouse", "product", "quantity", "created_at", "updated_at")
