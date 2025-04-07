from django.db import models

from apps.core.models import SoftDeleteModel, SafeDeleteManager
from apps.documents.models import Product
from apps.organizations.models import Organization


class Warehouse(SoftDeleteModel):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="warehouses",
    )
    name = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    is_trade = models.BooleanField(default=False)

    objects = SafeDeleteManager()
    all_objects = models.Manager()

    def __str__(self):
        return self.name


class ProductStock(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} (Warehouse: {self.warehouse.name})"
