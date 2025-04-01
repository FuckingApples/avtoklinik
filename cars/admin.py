from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'production_year', 'plate_number', 'mileage', 'price')  # "year" yerine "production_year" yaz
