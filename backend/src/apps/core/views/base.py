from rest_framework import filters
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from apps.core.mixins import OrganizationMixin


class BasePagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 100


class BaseOrganizationModelView(OrganizationMixin, ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = BasePagination
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    )
    serializer_class = None
    ordering = "-created_at"


class BaseOrganizationDetailView(OrganizationMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = None
    lookup_field = "id"
