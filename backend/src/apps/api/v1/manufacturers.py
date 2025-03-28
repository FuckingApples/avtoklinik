from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from apps.manufacturers.models import Manufacturer
from apps.organizations.models import Organization
from apps.api.serializers.manufacturers import ManufacturerSerializer

class ManufacturerBaseView:
    """Базовый класс для проверки доступа к организации"""
    permission_classes = [IsAuthenticated]

    def get_organization(self):
        org = get_object_or_404(
            Organization.all_objects,  # Используем all_objects для доступа ко всем организациям
            pk=self.kwargs['organization_id']
        )
        # Здесь можно добавить проверку прав пользователя
        return org

class ManufacturerListView(ManufacturerBaseView, generics.ListAPIView):
    serializer_class = ManufacturerSerializer

    def get_queryset(self):
        return Manufacturer.objects.filter(
            organization=self.get_organization(),
            is_deleted=False
        )

class ManufacturerCreateView(ManufacturerBaseView, generics.CreateAPIView):
    serializer_class = ManufacturerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organization=self.get_organization())
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ManufacturerDetailView(ManufacturerBaseView, generics.RetrieveAPIView):
    serializer_class = ManufacturerSerializer
    lookup_url_kwarg = 'manufacturer_id'

    def get_queryset(self):
        return Manufacturer.objects.filter(
            organization=self.get_organization(),
            is_deleted=False
        )

class ManufacturerUpdateView(ManufacturerBaseView, generics.UpdateAPIView):
    serializer_class = ManufacturerSerializer
    lookup_url_kwarg = 'manufacturer_id'

    def get_queryset(self):
        return Manufacturer.objects.filter(
            organization=self.get_organization(),
            is_deleted=False
        )

class ManufacturerDeleteView(ManufacturerBaseView, generics.DestroyAPIView):
    lookup_url_kwarg = 'manufacturer_id'

    def get_queryset(self):
        return Manufacturer.objects.filter(
            organization=self.get_organization(),
            is_deleted=False
        )

    def perform_destroy(self, instance):
        instance.soft_delete()  # Мягкое удаление вместо физического
