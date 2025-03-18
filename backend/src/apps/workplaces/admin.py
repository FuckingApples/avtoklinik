from django.contrib import admin

from apps.workplaces.models import Workplace


@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "color")
    search_fields = ("name", "color")
