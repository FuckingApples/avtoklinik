from django.urls import path

from apps.clients.models import Client
from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.api.serializers.clients import ClientSerializer


class OrganizationClientsAPI(BaseOrganizationModelView):
    model = Client
    serializer_class = ClientSerializer


class ClientsAPI(BaseOrganizationDetailView):
    model = Client
    serializer_class = ClientSerializer
    lookup_field = "client_id"


urlpatterns = [
    path(
        "",
        OrganizationClientsAPI.as_view(),
        name="organization_clients",
    ),
    path(
        "<int:client_id>/",
        ClientsAPI.as_view(),
        name="clients",
    ),
]
