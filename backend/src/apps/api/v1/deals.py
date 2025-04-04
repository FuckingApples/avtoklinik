from django.urls import path

from apps.api.serializers.deals import DealSerializer
from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.deals.models import Deal


class OrganizationDealsAPI(BaseOrganizationModelView):
    model = Deal
    serializer_class = DealSerializer


class DealsAPI(BaseOrganizationDetailView):
    model = Deal
    serializer_class = DealSerializer
    lookup_field = "deal_id"


urlpatterns = [
    path(
        "",
        OrganizationDealsAPI.as_view(),
        name="organization_deals",
    ),
    path(
        "<int:deal_id>/",
        DealsAPI.as_view(),
        name="deals",
    ),
]
