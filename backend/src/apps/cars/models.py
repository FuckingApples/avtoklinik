from django.db import models

from apps.organizations.models import Organization


class Car(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    frame = models.TextField(unique=True, null=True, blank=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30, null=True, blank=True)
    license_plate = models.CharField(max_length=15)
    license_plate_region = models.CharField(max_length=2)
    mileage = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
