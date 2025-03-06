from django.contrib import admin

from apps.oauth.models import OAuthProvider


class OAuthProviderAdmin(admin.ModelAdmin):
    readonly_fields = ("user", "provider", "uid")
    list_display = ("user", "provider", "created_at")
    list_filter = ("user", "provider")
    search_fields = ("user__email", "user__first_name", "user__last_name")


admin.site.register(OAuthProvider, OAuthProviderAdmin)
