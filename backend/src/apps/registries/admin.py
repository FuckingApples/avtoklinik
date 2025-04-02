from django.contrib import admin

from .models import Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "is_deleted", "created_at")
    list_filter = ("is_deleted", "organization", "created_at")
    search_fields = ("name", "description", "organization__name")
    list_select_related = ("organization",)
    ordering = ("name",)
    actions = ("soft_delete_selected", "restore_selected")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (None, {"fields": ("name", "organization", "description")}),
        (
            "System Information",
            {
                "fields": ("is_deleted", "created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )
