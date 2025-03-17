from django.db import models

from apps.organizations.models import Organization


class Workplace(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="workplaces",
    )
    icon = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name
