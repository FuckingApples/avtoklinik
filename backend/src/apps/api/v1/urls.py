from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api.v1.oauth import OAuthProviderViewSet

router = DefaultRouter()
router.register("oauth", OAuthProviderViewSet, basename="oauth")

urlpatterns = [
    path("user/", include("apps.api.v1.users")),
    path("organization/", include("apps.api.v1.organizations")),
    path("organization/<int:organization_id>/clients/", include("apps.api.v1.clients")),
    path("organization/<int:organization_id>/cars/", include("apps.api.v1.cars")),
    path(
        "organization/<int:organization_id>/warehouses/",
        include("apps.api.v1.warehouses"),
    ),
    path(
        "organization/<int:organization_id>/workplaces/",
        include("apps.api.v1.workplaces"),
    ),
    path("organization/<int:organization_id>/deals/", include("apps.api.v1.deals")),
    path(
        "organization/<int:organization_id>/registries/",
        include("apps.api.v1.registries"),
    ),
    path("", include(router.urls)),
]
