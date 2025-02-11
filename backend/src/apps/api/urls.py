from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.api.v1.users import RegisterAPI

router = DefaultRouter()
# router.register("users", UserViewSet, basename="users")
urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/users/register", RegisterAPI.as_view(), name="register"),
]
