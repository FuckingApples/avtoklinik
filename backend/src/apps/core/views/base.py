from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from apps.core.mixins import OrganizationMixin


class BaseOrganizationModelView(OrganizationMixin, ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = None


class BaseOrganizationDetailView(OrganizationMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = None
    lookup_field = "id"
