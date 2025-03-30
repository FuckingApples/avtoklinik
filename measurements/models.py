from django.db import models

class MeasurementUnit(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)
    okei_code = models.CharField(max_length=10, blank=True, null=True)
    organization = models.CharField(max_length=100)  # Dummy field, replace with ForeignKey if needed

    def __str__(self):
        return f"{self.abbreviation} ({self.name})"
