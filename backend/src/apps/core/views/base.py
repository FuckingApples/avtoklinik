from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.organizations.models import Organization


class OrganizationMixin:
    def get_organization(self):
        return get_object_or_404(Organization, id=self.kwargs["organization_id"])


class BaseOrganizationModelView(OrganizationMixin, generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    model = None
    serializer_class = None

    def get_queryset(self):
        organization = self.get_organization()
        return self.model.objects.filter(organization=organization)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        organization = self.get_organization()
        serializer = self.serializer_class(
            data=request.data,
            context={"organization": organization, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BaseOrganizationDetailView(OrganizationMixin, generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    model = None
    serializer_class = None
    lookup_field = "id"

    def get_object(self):
        organization = self.get_organization()
        obj_id = self.kwargs[self.lookup_field]
        return get_object_or_404(self.model, id=obj_id, organization=organization)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(
            instance,
            data=request.data,
            partial=True,
            context={"organization": instance.organization, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
