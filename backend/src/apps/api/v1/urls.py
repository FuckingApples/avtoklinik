from django.urls import path
from . import measurements

urlpatterns = [
    path('measurements/', measurements.MeasurementUnitListCreateView.as_view(), name='measurementunit-list-create'),
    path('measurements/<int:pk>/', measurements.MeasurementUnitRetrieveUpdateDestroyView.as_view(), name='measurementunit-detail'),
]
