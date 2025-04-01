from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.measurements.views import MeasurementUnitViewSet  # doğru import yolu

router = DefaultRouter()
router.register(r'measurement-units', MeasurementUnitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
