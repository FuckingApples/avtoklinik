from django.db import models


class Car(models.Model):
    REGION_CHOICES = (
        ("ru", "RUS"),  # Россия
        ("by", "BY"),  # Беларусь
        ("kz", "KZ"),  # Казахстан
        ("am", "AM"),  # Армения
        ("az", "AZ"),  # Азербайджан
        ("ge", "GE"),  # Грузия
        ("kg", "KG"),  # Кыргызстан
        ("md", "MD"),  # Молдова
        ("tj", "TJ"),  # Таджикистан
        ("uz", "UZ"),  # Узбекистан
        ("ee", "EST"),  # Эстония
        ("lv", "LV"),  # Латвия
        ("lt", "LT"),  # Литва
        ("ua", "UA"),  # Украина
        ("de", "D"),  # Германия
        ("fr", "F"),  # Франция
        ("us", "USA"),  # США
        ("cn", "CHN"),  # Китай
        ("jp", "J"),  # Япония
        ("tr", "TR"),  # Турция
        ("ch", "CH"),  # Швейцария
        ("pl", "PL"),  # Польша
        ("in", "IND"),  # Индия
    )

    vin = models.CharField(max_length=17, unique=True)
    frame = models.TextField(unique=True, null=True, blank=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30, null=True, blank=True)
    license_plate = models.CharField(max_length=15)
    license_plate_region = models.CharField(max_length=5, choices=REGION_CHOICES)
    mileage = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
