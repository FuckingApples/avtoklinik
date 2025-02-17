from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.v1.otp import RequestEmailOTPAPI, VerifyEmailOTPAPI
from apps.api.v1.tokens import CustomTokenObtainPairAPI, CustomTokenRefreshAPI
from apps.api.v1.users import RegisterAPI

router = DefaultRouter()
# router.register("users", UserViewSet, basename="users")
urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/users/register", RegisterAPI.as_view(), name="register"),
    path("v1/email/verify", VerifyEmailOTPAPI.as_view(), name="verify_email"),
    path("v1/email/verify/get_otp", RequestEmailOTPAPI.as_view(), name="get_email_otp"),
    path("token", CustomTokenObtainPairAPI.as_view(), name="token_obtain_pair"),
    path("token/refresh", CustomTokenRefreshAPI.as_view(), name="token_refresh"),
]
