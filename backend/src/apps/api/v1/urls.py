from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api.v1.oauth import OAuthProviderViewSet
from apps.api.v1.requests import OrganizationRequestsAPI, RequestAPI

router = DefaultRouter()
router.register("oauth", OAuthProviderViewSet, basename="oauth")

urlpatterns = [
    path("deals/", include("apps.api.v1.deals")),
    path("registries/", include("apps.api.v1.registries")),
    path("", include(router.urls)),
path("<int:organization_id>/requests/", OrganizationRequestsAPI.as_view(), name="organization_requests"),
    path("<int:organization_id>/requests/<int:request_id>/", RequestAPI.as_view(), name="request_detail"),
]
