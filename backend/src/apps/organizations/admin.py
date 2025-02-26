from django.contrib import admin

from apps.organizations.models import Organization, Membership, PermissionFlags


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


class MembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "organization", "get_roles_display")

    def get_roles_display(self, obj):

        return ", ".join(
            permission
            for bit, permission in PermissionFlags.PERMISSION_CHOICES
            if obj.has_permission(bit)
        )

    get_roles_display.short_description = "Permissions"


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Membership, MembershipAdmin)
