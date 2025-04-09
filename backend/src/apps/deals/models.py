from django.db import models

from apps.core.models import SoftDeleteModel


class Deal(SoftDeleteModel):
    number = models.CharField(max_length=25)
    client = models.ForeignKey(
        "clients.Client", on_delete=models.CASCADE, related_name="deals"
    )
    car = models.ForeignKey(
        "cars.Car", on_delete=models.SET_NULL, null=True, blank=True
    )
    comment = models.TextField(null=True, blank=True)
    organization = models.ForeignKey(
        "organizations.Organization", on_delete=models.CASCADE, related_name="deals"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Deal № {self.number} (Organization: {self.organization}, Client: {self.client})"


class ClientRequest(models.Model):
    number = models.CharField(max_length=25)
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="client_requests",
    )
    deal = models.ForeignKey(
        Deal,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="client_requests",
    )
    employee = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True, blank=True
    )
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE)
    workplace = models.ForeignKey(
        "registries.Workplace", on_delete=models.SET_NULL, null=True
    )
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request № {self.number} (Organization: {self.organization.name})"
