from django.urls import path
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.api.serializers.organizations import OrganizationSerializer
from apps.organizations.models import Organization, Role, Membership
from apps.organizations.permissions import HasRole


class OrganizationsAPI(generics.ListCreateAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated,)

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


class OrganizationPublicIdAPI(generics.RetrieveAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = "public_id"
    lookup_field = "public_id"

    def get_queryset(self):
        return Organization.objects.filter(membership__user=self.request.user)


urlpatterns = [
    path("", OrganizationsAPI.as_view(), name="organizations"),
    path(
        "<int:organization_id>/",
        OrganizationDetailsAPI.as_view(),
        name="organization_details",
    ),
    path(
        "by_public_id/<uuid:public_id>/",
        OrganizationPublicIdAPI.as_view(),
        name="organization_by_public_id",
    ),
]
