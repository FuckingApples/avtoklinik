from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from apps.api.v1.core import get_csrf_token
from apps.api.v1.oauth import YandexOAuthAPI, OAuthProviderViewSet
from apps.api.v1.organizations import CreateOrgAPI, DeleteOrgAPI
from apps.api.v1.otp import RequestEmailOTPAPI, VerifyEmailOTPAPI
from apps.api.v1.tokens import CustomTokenObtainPairAPI, CustomTokenRefreshAPI
from apps.api.v1.users import RegisterUserAPI, LogoutUserAPI, UserInfoAPI

from apps.api.v1.clients import (
    ClientListView,
    ClientCreateView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView,
)

from apps.api.v1.cars import (
    CarListView,
    CarCreateView,
    CarDetailView,
    CarUpdateView,
    CarDeleteView,
)

from apps.api.v1.warehouses import (
    WarehouseListView,
    WarehouseCreateView,
    WarehouseDetailView,
    WarehouseUpdateView,
    WarehouseDeleteView,
)

from apps.api.v1.workplaces import (
    WorkplaceListView,
    WorkplaceCreateView,
    WorkplaceDetailView,
    WorkplaceUpdateView,
    WorkplaceDeleteView,
)

# Default router
router = DefaultRouter()
router.register("oauth", OAuthProviderViewSet, basename="oauth")

urlpatterns = [
    # Swagger documentation routes
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-docs"
    ),
    # Users routes
    path("v1/user/", UserInfoAPI.as_view(), name="user_info"),
    path("v1/user/register/", RegisterUserAPI.as_view(), name="register"),
    path("v1/user/logout/", LogoutUserAPI.as_view(), name="logout"),
    path("v1/user/email/verify/", VerifyEmailOTPAPI.as_view(), name="verify_email"),
    path(
        "v1/user/email/verify/get_otp/",
        RequestEmailOTPAPI.as_view(),
        name="get_email_otp",
    ),
    # Organizations routes
    path("v1/organization/create/", CreateOrgAPI.as_view(), name="create_org"),
    path(
        "v1/organization/<int:organization_id>/delete/",
        DeleteOrgAPI.as_view(),
        name="delete_org",
    ),
    # Clients routes
    path(
        "v1/client/<int:organization_id>/", ClientListView.as_view(), name="client-list"
    ),
    path(
        "v1/client/<int:organization_id>/create/",
        ClientCreateView.as_view(),
        name="client-create",
    ),
    path(
        "v1/client/<int:organization_id>/<int:client_id>/",
        ClientDetailView.as_view(),
        name="client-detail",
    ),
    path(
        "v1/client/<int:organization_id>/<int:client_id>/update/",
        ClientUpdateView.as_view(),
        name="client-update",
    ),
    path(
        "v1/client/<int:organization_id>/<int:client_id>/delete/",
        ClientDeleteView.as_view(),
        name="client-delete",
    ),
    # Cars routes
    path("v1/auto/<int:organization_id>/", CarListView.as_view(), name="car-list"),
    path(
        "v1/auto/<int:organization_id>/create/",
        CarCreateView.as_view(),
        name="car-create",
    ),
    path(
        "v1/auto/<int:organization_id>/<int:car_id>/",
        CarDetailView.as_view(),
        name="car-detail",
    ),
    path(
        "v1/auto/<int:organization_id>/<int:car_id>/update/",
        CarUpdateView.as_view(),
        name="car-update",
    ),
    path(
        "v1/auto/<int:organization_id>/<int:car_id>/delete/",
        CarDeleteView.as_view(),
        name="car-delete",
    ),
    # Warehouses routes
    path(
        "v1/warehouse/<int:organization_id>/",
        WarehouseListView.as_view(),
        name="warehouse-list",
    ),
    path(
        "v1/warehouse/<int:organization_id>/create/",
        WarehouseCreateView.as_view(),
        name="warehouse-create",
    ),
    path(
        "v1/warehouse/<int:organization_id>/<int:warehouse_id>/",
        WarehouseDetailView.as_view(),
        name="warehouse-detail",
    ),
    path(
        "v1/warehouse/<int:organization_id>/<int:warehouse_id>/update/",
        WarehouseUpdateView.as_view(),
        name="warehouse-update",
    ),
    path(
        "v1/warehouse/<int:organization_id>/<int:warehouse_id>/delete/",
        WarehouseDeleteView.as_view(),
        name="warehouse-delete",
    ),
    # Workplaces routes
    path(
        "v1/workplace/<int:organization_id>/",
        WorkplaceListView.as_view(),
        name="workplace-list",
    ),
    path(
        "v1/workplace/<int:organization_id>/create/",
        WorkplaceCreateView.as_view(),
        name="workplace-create",
    ),
    path(
        "v1/workplace/<int:organization_id>/<int:workplace_id>/",
        WorkplaceDetailView.as_view(),
        name="workplace-detail",
    ),
    path(
        "v1/workplace/<int:organization_id>/<int:workplace_id>/update/",
        WorkplaceUpdateView.as_view(),
        name="workplace-update",
    ),
    path(
        "v1/workplace/<int:organization_id>/<int:workplace_id>/delete/",
        WorkplaceDeleteView.as_view(),
        name="workplace-delete",
    ),
    # JWT tokens routes
    path("token/", CustomTokenObtainPairAPI.as_view(), name="token_obtain_pair"),
    path("token/refresh/", CustomTokenRefreshAPI.as_view(), name="token_refresh"),
    # CSRF token
    path("csrf_token/", get_csrf_token, name="get_csrf_token"),
    # OAuth routes
    path("v1/oauth/yandex/", YandexOAuthAPI.as_view(), name="yandex_oauth"),
    path("v1/", include("apps.api.v1.urls")),  # Include v1 urls
    path("api/", include(router.urls)),  # OAuth router
]
