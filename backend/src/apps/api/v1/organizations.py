from django.urls import path
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.api.serializers.organizations import OrganizationSerializer
from apps.core.views.base import BasePagination
from apps.organizations.models import Organization, Role, Membership
from apps.organizations.permissions import HasRole


class OrganizationsAPI(generics.ListCreateAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = BasePagination

    def get_queryset(self):
        return Organization.objects.filter(membership__user=self.request.user)

    def perform_create(self, serializer):
        organization = serializer.save()
        Membership.objects.create(
            organization=organization, user=self.request.user, role=Role.OWNER
        )


class OrganizationDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated, HasRole)
    lookup_url_kwarg = "organization_id"

    required_roles = {
        "PATCH": [Role.OWNER, Role.ADMIN],
        "DELETE": [Role.OWNER],
    }

    def get_queryset(self):
        return Organization.objects.filter(membership__user=self.request.user)

    def perform_destroy(self, instance):
        instance.soft_delete()


urlpatterns = [
    path("", OrganizationsAPI.as_view(), name="organizations"),
    path(
        "<int:organization_id>/",
        OrganizationDetailsAPI.as_view(),
        name="organization_details",
    ),
]
