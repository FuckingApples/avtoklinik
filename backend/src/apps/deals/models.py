from django.db import models

from apps.cars.models import Car
from apps.clients.models import Client
from apps.core.models import SoftDeleteModel, SafeDeleteManager
from apps.organizations.models import Organization


class Deal(SoftDeleteModel):
    number = models.CharField(max_length=25)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    objects = SafeDeleteManager()
    all_objects = models.Manager()

    def __str__(self):
        return f"Deal № {self.number} (Organization: {self.organization}, Client: {self.client})"
