from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.v1.oauth import OAuthProviderViewSet

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
        "organizations/<int:organization_id>/works/",
        include("apps.api.v1.works"),
    ),
    path("", include(router.urls)),
]
