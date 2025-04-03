from dataclasses import dataclass
from rest_framework import serializers
from apps.documets.models import Documents
from apps.registries.models import Category
from apps.MeasurementUnit.models import MeasurementUnit
from apps.manufacturers.models import Manufacturer

@dataclass
class ProductDTO:
    name: str
    cheque_Name: str
    article: str = None
    barcode: str = None
    quantity: int = 1
    cost_price: float = 0.0
    selling_price: float = 0.0
    max_discount: int = 0
    critical_stock: int = 1
    desired_stock: int = 1
    net_weight: float = 0.0
    gross_weight: float = 0.0
    Country: str = None
    category_id: int = None
    sales_unit_id: int = None
    write_off_unit_id: int = None
    manufacturer_id: int = None
    id: int = None

    @classmethod
    def from_instance(cls, product: "Product") -> "ProductDTO":
        return cls(
            id=product.id,
            name=product.name,
            cheque_Name=product.cheque_Name,
            article=product.article,
            barcode=product.barcode,
            quantity=product.quantity,
            cost_price=product.cost_price,
            selling_price=product.selling_price,
            max_discount=product.max_discount,
            critical_stock=product.critical_stock,
            desired_stock=product.desired_stock,
            net_weight=product.net_weight,
            gross_weight=product.gross_weight,
            Country=product.Country,
            category_id=product.category.id if product.category else None,
            sales_unit_id=product.sales_unit.id if product.sales_unit else None,
            write_off_unit_id=product.write_off_unit.id if product.write_off_unit else None,
            manufacturer_id=product.manufacturer.id if product.manufacturer else None,
        )

class DocumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documents
        fields = (
            "id", "organization", "name", "cheque_Name", "article", "barcode", "quantity",
            "unit", "cost_price", "selling_price", "max_discount", "critical_stock",
            "desired_stock", "net_weight", "gross_weight", "Country", "category", "sales_unit",
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

