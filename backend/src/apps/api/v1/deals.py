from django.urls import path
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.api.serializers.deals import DealSerializer
from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.deals.models import Deal


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
    model = Deal
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
