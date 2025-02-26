from django.contrib import admin
from .models import User, UserOTP
from ..organizations.models import Membership


class MembershipInline(admin.StackedInline):
    model = Membership
    extra = 1


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_email_verified",
    )
    list_filter = ("is_active", "is_email_verified", "is_staff")
    search_fields = ("email", "first_name", "last_name", "id")
    inlines = [MembershipInline]


class UserOTPAdmin(admin.ModelAdmin):
    list_display = ("user", "otp_secret", "lifetime", "is_verified")
    list_filter = ("is_verified",)
    readonly_fields = ("otp_secret", "is_verified")


admin.site.register(User, UserAdmin)
admin.site.register(UserOTP, UserOTPAdmin)
