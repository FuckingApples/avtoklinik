from django.urls import path
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from apps.clients.models import Client
from apps.organizations.models import Organization
from apps.api.serializers.clients import ClientSerializer


class ClientListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        return Client.objects.filter(organization_id=organization_id)


class ClientCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        organization_id = self.kwargs.get("organization_id")
        organization = get_object_or_404(Organization, id=organization_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organization=organization)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ClientDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer
    lookup_url_kwarg = "client_id"

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        return Client.objects.filter(organization_id=organization_id)


class ClientUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer
    lookup_url_kwarg = "client_id"

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        return Client.objects.filter(organization_id=organization_id)


class ClientDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "client_id"

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        return Client.objects.filter(organization_id=organization_id)


urlpatterns = [
    path("", ClientListView.as_view(), name="client-list"),
    path(
        "create/",
        ClientCreateView.as_view(),
        name="client-create",
    ),
    path(
        "<int:client_id>/",
        ClientDetailView.as_view(),
        name="client-detail",
    ),
    path(
        "<int:client_id>/update/",
        ClientUpdateView.as_view(),
        name="client-update",
    ),
    path(
        "<int:client_id>/delete/",
        ClientDeleteView.as_view(),
        name="client-delete",
    ),
]
