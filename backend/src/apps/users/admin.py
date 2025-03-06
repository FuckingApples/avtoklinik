from django.contrib import admin
from .models import User, UserOTP
from ..oauth.models import OAuthProvider
from ..organizations.models import Membership


# Inline-модели для отображения связанных объектов в админке
class MembershipInline(admin.StackedInline):
    model = Membership
    extra = 1


class OAuthProviderInline(admin.TabularInline):
    model = OAuthProvider
    extra = 0
    readonly_fields = ("provider", "uid")
    can_delete = False


# Классы для отображения моделей в админке
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_email_verified",
        "has_usable_password",
    )
    list_filter = ("is_active", "is_email_verified", "is_staff")
    search_fields = ("email", "first_name", "last_name", "id")
    inlines = [MembershipInline, OAuthProviderInline]


class UserOTPAdmin(admin.ModelAdmin):
    list_display = ("user", "otp_secret", "lifetime", "is_verified")
    list_filter = ("is_verified",)
    readonly_fields = ("otp_secret", "is_verified")


# Регистрация моделей в админке
admin.site.register(User, UserAdmin)
admin.site.register(UserOTP, UserOTPAdmin)
