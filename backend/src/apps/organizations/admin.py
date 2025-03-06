from django.contrib import admin

from apps.organizations.models import Organization, Membership, PermissionFlags, Role


# Классы для отображения моделей в админке
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


class MembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "organization", "role", "get_permissions_display")
    search_fields = ("organization__name", "role__name", "user__email")
    list_filter = ("role", "organization")

    def get_permissions_display(self, obj):

        return ", ".join(
            permission
            for bit, permission in PermissionFlags.PERMISSION_CHOICES
            if obj.has_permission(bit)
        )

    get_permissions_display.short_description = "Permissions"


class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "default_permissions")
    search_fields = ("name",)


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Role, RoleAdmin)
