from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from apps.documets.models import Documents
from apps.organizations.models import Organization
from apps.api.serializers.documents import DocumentsSerializer


class DocumentsListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentsSerializer

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        return Documents.objects.filter(organization_id=organization_id)


class DocumentsCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentsSerializer

    def create(self, request, *args, **kwargs):
        organization_id = self.kwargs.get("organization_id")
        organization = get_object_or_404(Organization, id=organization_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organization=organization)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentsSerializer
    lookup_url_kwarg = "product_id"

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        return Documents.objects.filter(organization_id=organization_id)


class DocumentsUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentsSerializer
    lookup_url_kwarg = "product_id"

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        return Documents.objects.filter(organization_id=organization_id)


class DocumentsDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "product_id"

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        return Documents.objects.filter(organization_id=organization_id)