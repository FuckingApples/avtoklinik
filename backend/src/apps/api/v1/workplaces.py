from django.urls import path
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.workplaces.models import Workplace
from apps.api.serializers.workplaces import WorkplaceSerializer


@extend_schema(tags=["Рабочие места"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание рабочего места",
        request=WorkplaceSerializer,
        responses={status.HTTP_201_CREATED: WorkplaceSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех рабочих мест организации",
        responses={status.HTTP_200_OK: WorkplaceSerializer},
    ),
)
class OrganizationWorkplacesAPI(BaseOrganizationModelView):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


@extend_schema(tags=["Рабочие места"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление рабочего места",
        request=WorkplaceSerializer,
        responses={status.HTTP_200_OK: WorkplaceSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о рабочем месте",
        responses={status.HTTP_200_OK: WorkplaceSerializer},
    ),
    delete=extend_schema(
        summary="Удаление рабочего места",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class WorkplacesAPI(BaseOrganizationDetailView):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


urlpatterns = [
    path(
        "",
        OrganizationWorkplacesAPI.as_view(),
        name="organization_workplaces",
    ),
    path(
        "<int:id>/",
        WorkplacesAPI.as_view(),
        name="workplaces",
    ),
]
