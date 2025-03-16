from django.contrib import admin

from apps.oauth.models import OAuthProvider


@admin.register(OAuthProvider)
class OAuthProviderAdmin(admin.ModelAdmin):
    list_display = ("user", "provider", "created_at")
    list_filter = ("provider",)
    search_fields = ("user__email", "user__first_name", "user__last_name")

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
