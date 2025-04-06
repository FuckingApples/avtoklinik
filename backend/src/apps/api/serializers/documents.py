from apps.core.serializers import BaseOrganizationModelSerializer
from apps.documents.models import Product


class ProductSerializer(BaseOrganizationModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "organization",
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
        )
