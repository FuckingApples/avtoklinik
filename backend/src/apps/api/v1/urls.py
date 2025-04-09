from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api.v1.oauth import OAuthProviderViewSet
from apps.api.v1.requests import OrganizationRequestsAPI, RequestAPI

router = DefaultRouter()
router.register("oauth", OAuthProviderViewSet, basename="oauth")

urlpatterns = [
    path("user/", include("apps.api.v1.users")),
    path("organizations/", include("apps.api.v1.organizations")),
    path(
        "organizations/<int:organization_id>/clients/", include("apps.api.v1.clients")
    ),
    path("organizations/<int:organization_id>/cars/", include("apps.api.v1.cars")),
    path(
        "organizations/<int:organization_id>/warehouses/",
        include("apps.api.v1.warehouses"),
    ),
    path("organizations/<int:organization_id>/deals/", include("apps.api.v1.deals")),
    path(
        "organizations/<int:organization_id>/registries/",
        include("apps.api.v1.registries"),
    ),
    path(
        "organizations/<int:organization_id>/products/",
        include("apps.api.v1.documents"),
    ),
    path("", include(router.urls)),
    path("<int:organization_id>/requests/", OrganizationRequestsAPI.as_view(), name="organization_requests"),
    path("<int:organization_id>/requests/<int:request_id>/", RequestAPI.as_view(), name="request_detail"),
]
