from django.urls import path

from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.workplaces.models import Workplace
from apps.api.serializers.workplaces import WorkplaceSerializer


class OrganizationWorkplacesAPI(BaseOrganizationModelView):
    model = Workplace
    serializer_class = WorkplaceSerializer


class WorkplacesAPI(BaseOrganizationDetailView):
    model = Workplace
    serializer_class = WorkplaceSerializer
    lookup_field = "workplace_id"


urlpatterns = [
    path(
        "",
        OrganizationWorkplacesAPI.as_view(),
        name="organization_workplaces",
    ),
    path(
        "<int:workplace_id>/",
        WorkplacesAPI.as_view(),
        name="workplaces",
    ),
]
