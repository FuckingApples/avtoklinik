from django.db import models

from apps.core.models import SafeDeleteManager
from apps.organizations.models import Organization


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subcategories",
        null=True,
        blank=True,
    )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = SafeDeleteManager()
    all_objects = models.Manager()

    def __str__(self):
        return f"{self.name} (Org: {self.organization.public_id})"

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()


class MeasurementUnit(models.Model):
    unit = models.TextField()
    abbreviation = models.CharField(max_length=100)
    okei_code = models.PositiveSmallIntegerField(blank=True, null=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="measurement_units"
    )

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.TextField()
    hex = models.CharField(max_length=7, blank=True, null=True)
    code = models.CharField(max_length=25, blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
