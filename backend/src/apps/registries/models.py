from django.core.validators import MinValueValidator
from django.db import models

from apps.core.models import unique_org_fields


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subcategories",
        null=True,
        blank=True,
    )
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="categories",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = unique_org_fields("Category", "name")

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="manufacturers",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = unique_org_fields("Manufacturer", "name")

    def __str__(self):
        return f"{self.name} (Org: {self.organization.public_id})"


class MeasurementUnit(models.Model):
    unit = models.TextField()
    abbreviation = models.CharField(max_length=100)
    okei_code = models.PositiveSmallIntegerField(blank=True, null=True)
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="measurement_units",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = unique_org_fields("MeasurementUnit", "unit", "abbreviation")

    def __str__(self):
        return self.unit


class Color(models.Model):
    name = models.TextField()
    hex = models.CharField(max_length=7, blank=True, null=True)
    code = models.CharField(max_length=25, blank=True, null=True)
    organization = models.ForeignKey(
        "organizations.Organization", on_delete=models.CASCADE, related_name="colors"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = unique_org_fields("Color", "name")

    def __str__(self):
        return self.name


class Workplace(models.Model):
    icon = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=7)
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="workplaces",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = unique_org_fields("Workplace", "name")

    def __str__(self):
        return self.name


class HourlyWage(models.Model):
    name = models.CharField(max_length=100)
    wage = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="hourly_wages",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = unique_org_fields("HourlyWage", "name")

    def __str__(self):
        return f"{self.name} ({self.wage} руб.)"
