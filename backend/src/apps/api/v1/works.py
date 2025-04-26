from django.urls import path
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.api.serializers.works import WorkSerializer
from apps.core.views.base import BaseOrganizationDetailView, BaseOrganizationModelView
from apps.works.models import Work


@extend_schema(tags=["Работы"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание работы",
        request=WorkSerializer,
        responses={status.HTTP_201_CREATED: WorkSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех работ организации",
        responses={status.HTTP_200_OK: WorkSerializer},
    ),
)
class OrganizationWorksAPI(BaseOrganizationModelView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


@extend_schema(tags=["Работы"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление работы",
        request=WorkSerializer,
        responses={status.HTTP_200_OK: WorkSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о работе",
        responses={status.HTTP_200_OK: WorkSerializer},
    ),
    delete=extend_schema(
        summary="Удаление работы",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class WorkAPI(BaseOrganizationDetailView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


urlpatterns = [
    path(
        "",
        OrganizationWorksAPI.as_view(),
        name="organization_works",
    ),
    path(
        "<int:id>/",
        WorkAPI.as_view(),
        name="works",
    ),
]
