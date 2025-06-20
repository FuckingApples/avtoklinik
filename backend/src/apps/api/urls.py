from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from apps.api.v1.core import get_csrf_token
from apps.api.v1.otp import RequestEmailOTPAPI, VerifyEmailOTPAPI
from apps.api.v1.tokens import CustomTokenObtainPairAPI, CustomTokenRefreshAPI

router = DefaultRouter()

urlpatterns = [
    # Swagger documentation routes
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-docs"
    ),
    # Users routes
    path("v1/user/email/verify/", VerifyEmailOTPAPI.as_view(), name="verify_email"),
    path(
        "v1/user/email/verify/get_otp/",
        RequestEmailOTPAPI.as_view(),
        name="get_email_otp",
    ),
    # JWT tokens routes
    path("token/", CustomTokenObtainPairAPI.as_view(), name="token_obtain_pair"),
    path("token/refresh/", CustomTokenRefreshAPI.as_view(), name="token_refresh"),
    # CSRF token
    path("csrf_token/", get_csrf_token, name="get_csrf_token"),
    path("v1/", include("apps.api.v1.urls")),
]
