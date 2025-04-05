from django.urls import path
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.clients.models import Client
from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.api.serializers.clients import ClientSerializer


@extend_schema(tags=["Клиенты"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание клиента",
        request=ClientSerializer,
        responses={status.HTTP_201_CREATED: ClientSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех клиентов организации",
        responses={status.HTTP_200_OK: ClientSerializer},
    ),
)
class OrganizationClientsAPI(BaseOrganizationModelView):
    model = Client
    serializer_class = ClientSerializer


@extend_schema(tags=["Клиенты"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление клиента",
        request=ClientSerializer,
        responses={status.HTTP_200_OK: ClientSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о клиенте",
        responses={status.HTTP_200_OK: ClientSerializer},
    ),
    delete=extend_schema(
        summary="Удаление клиента",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
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
