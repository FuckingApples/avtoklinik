from django.contrib import admin

from .models import Template


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ("field_id", "is_organization", "created_at", "updated_at")
    search_fields = ("field_id", "text")
    list_filter = ("is_organization",)
