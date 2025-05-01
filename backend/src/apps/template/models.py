from django.db import models


class Template(models.Model):
    is_organization = models.BooleanField(default=False, help_text="Привязан ли шаблон к организации")
    text = models.TextField(help_text="Текст шаблона")
    field_id = models.CharField(max_length=255, help_text="ID связанного поля")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Шаблон"
        verbose_name_plural = "Шаблоны"

    def __str__(self):
        return f"{self.field_id} — {'Org' if self.is_organization else 'User'}"
