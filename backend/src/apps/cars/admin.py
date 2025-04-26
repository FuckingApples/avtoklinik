from django.contrib import admin

from apps.cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "vin",
        "frame",
        "__str__",
        "mileage",
        "license_plate",
    )
    search_fields = ("license_plate", "vin", "model", "brand")
    list_filter = ("year",)
    date_hierarchy = "created_at"
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "vin",
                    "frame",
                    "year",
                    "mileage",
                    ("brand", "model", "color"),
                    "license_plate",
                    "organization",
                ),
            },
        ),
    )
