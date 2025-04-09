from django.db import models

from apps.core.models import SoftDeleteModel


class Warehouse(SoftDeleteModel):
    name = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    is_trade = models.BooleanField(default=False)
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="warehouses",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductStock(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey("documents.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="product_stocks",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} (Warehouse: {self.warehouse.name})"
