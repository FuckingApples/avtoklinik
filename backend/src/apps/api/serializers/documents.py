from dataclasses import dataclass

from rest_framework import serializers
from apps.documets.models import Documents
from apps.registries.models import Category
from apps.MeasurementUnit.models import MeasurementUnit
from apps.manufacturers.models import Manufacturer

@dataclass
class DocumentsDTO:
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
    def from_instance(cls, doc: "Documents") -> "DocumentsDTO":
        return cls(
            id=doc.id,
            name=doc.name,
            cheque_Name=doc.cheque_Name,
            article=doc.article,
            barcode=doc.barcode,
            quantity=doc.quantity,
            cost_price=doc.cost_price,
            selling_price=doc.selling_price,
            max_discount=doc.max_discount,
            critical_stock=doc.critical_stock,
            desired_stock=doc.desired_stock,
            net_weight=doc.net_weight,
            gross_weight=doc.gross_weight,
            country=doc.country,
            comment=doc.comment,
            category_id=doc.category.id if doc.category else None,
            sales_unit_id=doc.sales_unit.id if doc.sales_unit else None,
            write_off_unit_id=doc.write_off_unit.id if doc.write_off_unit else None,
            manufacturer_id=doc.manufacturer.id if doc.manufacturer else None,
        )

class DocumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documents
        fields = (
            "id", "organization", "name", "cheque_Name", "article", "barcode", "quantity",
            "cost_price", "selling_price", "max_discount", "critical_stock",
            "desired_stock", "net_weight", "gross_weight", "country", "comment", "category", "sales_unit",
            "write_off_unit", "manufacturer"
        )

    def create(self, validated_data):
        category_data = validated_data.pop('category', None)
        sales_unit_data = validated_data.pop('sales_unit', None)
        write_off_unit_data = validated_data.pop('write_off_unit', None)
        manufacturer_data = validated_data.pop('manufacturer', None)

        doc = Documents.objects.create(**validated_data)

        if category_data:
            doc.category = Category.objects.get(id=category_data)

        if sales_unit_data:
            doc.sales_unit = MeasurementUnit.objects.get(id=sales_unit_data)

        if write_off_unit_data:
            doc.write_off_unit = MeasurementUnit.objects.get(id=write_off_unit_data)

        if manufacturer_data:
            doc.manufacturer = Manufacturer.objects.get(id=manufacturer_data)

        doc.save()

        return doc

