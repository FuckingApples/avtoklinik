from django.db import models

class Car(models.Model):
    vin = models.CharField(max_length=17, unique=True)  # Vehicle Identification Number
    brand = models.CharField(max_length=50)  # Brand
    model = models.CharField(max_length=50)  # Model
    production_year = models.IntegerField()  # Year of Production
    plate_number = models.CharField(max_length=20, unique=True, blank=True, null=True)  # License Plate Number
    mileage = models.PositiveIntegerField(default=0)  # Mileage (in km)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Price

    def __str__(self):
        return f"{self.brand} {self.model} ({self.production_year})"
