from django.db import models

class Calculation(models.Model):
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="calculations",
    )
    client = models.ForeignKey(
        "clients.Client",
        on_delete=models.CASCADE,
        related_name="calculations",
    )
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    car = models.ForeignKey(
        "cars.Car",
        on_delete=models.CASCADE,
    )
    responsible = models.CharField(max_length=100)

    calculation_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    deal = models.ForeignKey(
        "deals.Deal",
        on_delete=models.CASCADE,
        related_name="calculations",
    )
    special_notes = models.TextField(
        blank=True,
        null=True
    )
    productStock = models.ForeignKey(
        "warehouses.ProductStock",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    works = models.ForeignKey(
        "works.Work",
        on_delete=models.SET_NULL,
        related_name="calculations",
        blank=True,
        null=True
    )
    commentary = models.TextField(
        blank=True,
        null=True
    )