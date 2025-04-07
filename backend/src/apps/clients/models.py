from django.db import models

from apps.core.models import SoftDeleteModel


class Client(SoftDeleteModel):
    last_name = models.TextField()
    first_name = models.TextField()
    middle_name = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=12)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(
        "organizations.Organization", on_delete=models.CASCADE, related_name="clients"
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name if self.middle_name else ''}"
