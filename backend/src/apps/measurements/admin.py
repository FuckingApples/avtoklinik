from django.contrib import admin
from .models import MeasurementUnit

@admin.register(MeasurementUnit)
class MeasurementUnitAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "abbreviation", "okei_code", "organization")
    search_fields = ("name", "abbreviation", "okei_code")
