from django.db import models
from apps.organizations.models import Organization

class Manufacturer(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Manufacturer's name",
        help_text="Required field"
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        verbose_name="Organization",
        related_name="manufacturers"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturer's"
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'organization'],
                name='unique_manufacturer_name_per_organization'
            )
        ]

    def __str__(self):
        return f"{self.name} (Org: {self.organization.public_id})"

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()
