from django.urls import path

from apps.cars.models import Car
from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.api.serializers.cars import CarSerializer


class OrganizationCarsAPI(BaseOrganizationModelView):
    model = Car
    serializer_class = CarSerializer


class CarsAPI(BaseOrganizationDetailView):
    model = Car
    serializer_class = CarSerializer
    lookup_field = "car_id"


urlpatterns = [
    path(
        "",
        OrganizationCarsAPI.as_view(),
        name="organization_cars",
    ),
    path(
        "<int:car_id>/",
        CarsAPI.as_view(),
        name="cars",
    ),
]
