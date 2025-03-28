from django.db import models
from apps.organizations.models import Organization

class Manufacturer(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название производителя",
        help_text="Обязательное поле"
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        verbose_name="Организация",
        related_name="manufacturers"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  # Для согласованности с Organization

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
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
        """Мягкое удаление (аналогично Organization)"""
        self.is_deleted = True
        self.save()

    def restore(self):
        """Восстановление (аналогично Organization)"""
        self.is_deleted = False
        self.save()
