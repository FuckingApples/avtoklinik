from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from apps.api.v1.core import get_csrf_token
from apps.api.v1.oauth import YandexOAuthAPI, OAuthProviderViewSet
from apps.api.v1.otp import RequestEmailOTPAPI, VerifyEmailOTPAPI
from apps.api.v1.tokens import CustomTokenObtainPairAPI, CustomTokenRefreshAPI
from apps.api.v1.templates import TemplateListCreateAPI

router = DefaultRouter()
router.register("oauth", OAuthProviderViewSet, basename="oauth")

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
    # OAuth routes
    path("v1/oauth/yandex/", YandexOAuthAPI.as_view(), name="yandex_oauth"),
    path("v1/", include("apps.api.v1.urls")),
    path("templates/", TemplateListCreateAPI.as_view(), name="templates"),
]
