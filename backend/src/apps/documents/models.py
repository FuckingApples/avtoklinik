from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django_countries.fields import CountryField


class Product(models.Model):
    name = models.TextField()
    receipt_name = models.TextField()
    article = models.TextField(blank=True, null=True)
    barcode = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    sales_unit = models.ForeignKey(
        "registries.MeasurementUnit",
        on_delete=models.PROTECT,
        related_name="products_sales_unit",
    )
    write_off_unit = models.ForeignKey(
        "registries.MeasurementUnit",
        on_delete=models.PROTECT,
        related_name="products_write_off_unit",
    )
    selling_price = models.DecimalField(
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )
    cost_price = models.DecimalField(
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )
    max_discount = models.PositiveIntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        null=True,
        blank=True,
        default=0,
    )
    critical_stock = models.PositiveIntegerField(null=True, blank=True)
    desired_stock = models.PositiveIntegerField(null=True, blank=True)
    net_mass = models.DecimalField(
        null=True,
        blank=True,
        max_digits=16,
        decimal_places=6,
        validators=[MinValueValidator(0.000001)],
    )
    gross_mass = models.DecimalField(
        null=True,
        blank=True,
        max_digits=16,
        decimal_places=6,
        validators=[MinValueValidator(0.000001)],
    )
    manufacturer = models.ForeignKey(
        "registries.Manufacturer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    country = CountryField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        "registries.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="products",
    )

    def __str__(self):
        return self.name
