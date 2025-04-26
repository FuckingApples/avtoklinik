from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Work(models.Model):
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="works",
    )
    name = models.CharField(max_length=100)
    executor = models.ForeignKey(
        "organizations.Membership",
        on_delete=models.CASCADE,
        related_name="works",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        "registries.Category", on_delete=models.SET_NULL, blank=True, null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hourly_wage = models.ForeignKey(
        "registries.HourlyWage",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="works",
    )
    norm_time = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    max_discount = models.PositiveIntegerField(
        validators=[MaxValueValidator(100.0), MinValueValidator(0.0)],
        default=0,
    )
    coefficient = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1,
    )
    multiplicity = models.PositiveIntegerField(default=1)
    comment = models.TextField(blank=True, null=True)
    barcode = models.TextField(blank=True, null=True)
    work_code = models.TextField(blank=True, null=True)
    related_works = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name="related_to",
    )
    products = models.ManyToManyField(
        "warehouses.Product",
        blank=True,
        symmetrical=False,
        related_name="products",
    )

    def __str__(self):
        return self.name
