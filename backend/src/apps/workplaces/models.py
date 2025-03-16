from django.db import models


class Workplace(models.Model):
    icon = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name
