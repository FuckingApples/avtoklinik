from django.utils import timezone

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_countries.fields import CountryField

from apps.core.models import unique_org_fields


class Car(models.Model):
    vin = models.CharField(max_length=17)
    frame = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900.0),
            MaxValueValidator(timezone.now().year + 1.0),
        ]
    )
    color = models.ForeignKey(
        "registries.Color",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    client = models.ForeignKey(
        "clients.Client",
        null=True, 
        blank=True,
        on_delete=models.SET_NULL,
        related_name="cars"
    )
    license_plate = models.CharField(max_length=15)
    license_plate_region = CountryField()
    mileage = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(
        "organizations.Organization", on_delete=models.CASCADE, related_name="cars"
    )

    class Meta:
        constraints = unique_org_fields("Car", "vin", "frame", "license_plate")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
