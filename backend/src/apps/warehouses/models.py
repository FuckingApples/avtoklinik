from django.db import models

from apps.organizations.models import Organization


class Warehouse(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="warehouses",
    )
    name = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    is_trade = models.BooleanField(default=False)

    def __str__(self):
        return self.name
