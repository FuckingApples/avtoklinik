from django.urls import path, include
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.api.serializers.deals import DealSerializer, ClientRequestSerializer
from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.deals.models import Deal, ClientRequest


@extend_schema(tags=["Сделки"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание сделки",
        request=DealSerializer,
        responses={status.HTTP_201_CREATED: DealSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех сделок организации",
        responses={status.HTTP_200_OK: DealSerializer},
    ),
)
class OrganizationDealsAPI(BaseOrganizationModelView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer


@extend_schema(tags=["Сделки"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление сделки",
        request=DealSerializer,
        responses={status.HTTP_200_OK: DealSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о сделке",
        responses={status.HTTP_200_OK: DealSerializer},
    ),
    delete=extend_schema(
        summary="Удаление сделки",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class DealsAPI(BaseOrganizationDetailView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer


@extend_schema(tags=["Заявки"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание заявки",
        request=ClientRequestSerializer,
        responses={status.HTTP_201_CREATED: ClientRequestSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех заявок организации",
        responses={status.HTTP_200_OK: ClientRequestSerializer},
    ),
)
class OrganizationClientRequestsAPI(BaseOrganizationModelView):
    queryset = ClientRequest.objects.all()
    serializer_class = ClientRequestSerializer


@extend_schema(tags=["Заявки"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление заявки",
        request=ClientRequestSerializer,
        responses={status.HTTP_200_OK: ClientRequestSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о заявке",
        responses={status.HTTP_200_OK: ClientRequestSerializer},
    ),
    delete=extend_schema(
        summary="Удаление заявки",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class ClientRequestsAPI(BaseOrganizationDetailView):
    queryset = ClientRequest.objects.all()
    serializer_class = ClientRequestSerializer


deals_urls = [
    path(
        "",
        OrganizationDealsAPI.as_view(),
        name="organization_deals",
    ),
    path(
        "<int:id>/",
        DealsAPI.as_view(),
        name="deals",
    ),
]

client_requests_urls = [
    path(
        "",
        OrganizationClientRequestsAPI.as_view(),
        name="organization_client_requests",
    ),
    path(
        "<int:id>/",
        ClientRequestsAPI.as_view(),
        name="client_requests",
    ),
]

urlpatterns = [
    path("", include(deals_urls)),
    path("client_requests/", include(client_requests_urls)),
]
