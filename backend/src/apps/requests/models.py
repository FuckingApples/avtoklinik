from django.db import models
from apps.organizations.models import Organization
from apps.deals.models import Deal
from apps.users.models import User
from apps.registries.models import Workplace


class ServiceRequest(models.Model):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="service_requests"
    )
    number = models.CharField(max_length=50)
    deal = models.ForeignKey(
        Deal, on_delete=models.CASCADE, null=True, blank=True, related_name="requests"
    )
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("organization", "number")

    def __str__(self):
        return f"{self.organization.name} - {self.number}"
