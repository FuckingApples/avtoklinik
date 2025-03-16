from datetime import timedelta

from django.contrib import admin, messages
from .models import User, UserOTP
from ..oauth.models import OAuthProvider
from ..organizations.models import Membership


# Inline-модели для отображения связанных объектов в админке
class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1
    classes = ("collapse",)


class OAuthProviderInline(admin.TabularInline):
    model = OAuthProvider
    extra = 0
    readonly_fields = ("provider", "uid")
    can_delete = False

    def has_add_permission(self, request, obj):
        return False


# Классы для отображения моделей в админке
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "email",
        "is_active",
        "is_email_verified",
        "has_usable_password",
    )
    list_filter = ("is_active", "is_email_verified", "is_staff")
    list_editable = ("is_email_verified",)
    search_fields = ("email", "first_name", "last_name", "id")
    actions = ("activate_selected_users", "deactivate_selected_users")
    save_on_top = True
    inlines = (OAuthProviderInline, MembershipInline)

    def activate_selected_users(self, request, queryset):
        users = queryset.update(is_email_verified=True)
        messages.success(request, f"{users} users activated")

    def deactivate_selected_users(self, request, queryset):
        users = queryset.update(is_email_verified=False)
        messages.warning(request, f"{users} users deactivated")


@admin.register(UserOTP)
class UserOTPAdmin(admin.ModelAdmin):
    list_display = ("user", "get_lifetime", "is_verified")
    list_filter = ("is_verified",)

    @admin.display(description="OTP lifetime")
    def get_lifetime(self, obj: "UserOTP"):
        return timedelta(seconds=obj.lifetime)

    def has_add_permission(self, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False
