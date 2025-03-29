from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api.v1.oauth import OAuthProviderViewSet

router = DefaultRouter()
router.register("oauth", OAuthProviderViewSet, basename="oauth")

urlpatterns = [
    path("deals/", include("apps.api.v1.deals")),
    path("", include(router.urls)),
]
