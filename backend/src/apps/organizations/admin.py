from django.contrib import admin

from apps.organizations.models import Organization, Membership, PermissionFlags


# Классы для отображения моделей в админке
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "organization", "role", "get_permissions_display")
    search_fields = ("organization__name", "role", "user__email")
    list_filter = ("role", "organization")

    @admin.display(description="Permissions")
    def get_permissions_display(self, obj: "Membership"):
        return ", ".join(
            permission
            for bit, permission in PermissionFlags.PERMISSION_CHOICES
            if obj.has_permission(bit)
        )
