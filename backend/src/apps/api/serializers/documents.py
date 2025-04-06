from dataclasses import dataclass

from rest_framework import serializers
from apps.documents.models import Product
from apps.registries.models import Category
from apps.MeasurementUnit.models import MeasurementUnit
from apps.manufacturers.models import Manufacturer


@dataclass
class ProductDTO:
    name: str
    cheque_Name: str
    article: str = None
    barcode: str = None
    quantity: int = 0
    cost_price: float = None
    selling_price: float = None
    max_discount: int = None
    critical_stock: int = None
    desired_stock: int = None
    net_weight: float = None
    gross_weight: float = None
    country: str = None
    comment: str = None
    category_id: int = None
    sales_unit_id: int = 0
    write_off_unit_id: int = 0
    manufacturer_id: int = None
    id: int = 0

    @classmethod
    def from_instance(cls, prod: "Product") -> "ProductDTO":
        return cls(
            id=prod.id,
            name=prod.name,
            cheque_Name=prod.cheque_Name,
            article=prod.article,
            barcode=prod.barcode,
            quantity=prod.quantity,
            cost_price=prod.cost_price,
            selling_price=prod.selling_price,
            max_discount=prod.max_discount,
            critical_stock=prod.critical_stock,
            desired_stock=prod.desired_stock,
            net_weight=prod.net_weight,
            gross_weight=prod.gross_weight,
            country=prod.country,
            comment=prod.comment,
            category_id=prod.category.id if prod.category else None,
            sales_unit_id=prod.sales_unit.id if prod.sales_unit else None,
            write_off_unit_id=prod.write_off_unit.id if prod.write_off_unit else None,
            manufacturer_id=prod.manufacturer.id if prod.manufacturer else None,
        )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "organization",
            "name",
            "cheque_Name",
            "article",
            "barcode",
            "quantity",
            "cost_price",
            "selling_price",
            "max_discount",
            "critical_stock",
            "desired_stock",
            "net_weight",
            "gross_weight",
            "country",
            "comment",
            "category",
            "sales_unit",
            "write_off_unit",
            "manufacturer",
        )

    def create(self, validated_data):
        category_data = validated_data.pop("category", None)
        sales_unit_data = validated_data.pop("sales_unit", None)
        write_off_unit_data = validated_data.pop("write_off_unit", None)
        manufacturer_data = validated_data.pop("manufacturer", None)

        prod = Product.objects.create(**validated_data)

        if category_data:
            prod.category = Category.objects.get(id=category_data)

        if sales_unit_data:
            prod.sales_unit = MeasurementUnit.objects.get(id=sales_unit_data)

        if write_off_unit_data:
            prod.write_off_unit = MeasurementUnit.objects.get(id=write_off_unit_data)

        if manufacturer_data:
            prod.manufacturer = Manufacturer.objects.get(id=manufacturer_data)

        prod.save()

        return prod
