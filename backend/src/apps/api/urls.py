from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.api.v1.users import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
urlpatterns = [
    path('v1/', include(router.urls)),
]