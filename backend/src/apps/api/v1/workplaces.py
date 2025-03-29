from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from apps.workplaces.models import Workplace
from apps.organizations.models import Organization
from apps.api.serializers.workplaces import WorkplaceSerializer


class WorkplaceListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkplaceSerializer

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        return Workplace.objects.filter(organization_id=organization_id)


class WorkplaceCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkplaceSerializer

    def create(self, request, *args, **kwargs):
        organization_id = self.kwargs.get("organization_id")
        organization = get_object_or_404(Organization, id=organization_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organization=organization)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WorkplaceDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkplaceSerializer
    lookup_url_kwarg = "workplace_id"

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        return Workplace.objects.filter(organization_id=organization_id)


class WorkplaceUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkplaceSerializer
    lookup_url_kwarg = "workplace_id"

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        return Workplace.objects.filter(organization_id=organization_id)


class WorkplaceDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "workplace_id"

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        return Workplace.objects.filter(organization_id=organization_id)
