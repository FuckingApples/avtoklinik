from django.contrib import admin

from apps.clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "phone")
    search_fields = ("first_name", "last_name", "middle_name", "email")
