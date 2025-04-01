from django.db import models
from apps.organizations.models import Organization

class MeasurementUnit(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)
    okei_code = models.PositiveIntegerField(blank=True, null=True)  # ✅ DÜZELTİLDİ
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='measurement_units'
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'measurements'
