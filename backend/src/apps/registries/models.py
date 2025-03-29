from django.db import models

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
