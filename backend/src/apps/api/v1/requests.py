from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from apps.requests.models import ServiceRequest
from apps.organizations.models import Organization
from apps.api.serializers.requests import ServiceRequestSerializer

class OrganizationRequestsAPI(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, organization_id):
        get_object_or_404(Organization, id=organization_id)
        requests_qs = ServiceRequest.objects.filter(organization_id=organization_id)
        serializer = ServiceRequestSerializer(requests_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, organization_id):
        organization = get_object_or_404(Organization, id=organization_id)
        serializer = ServiceRequestSerializer(
            data=request.data,
            context={"organization": organization, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RequestAPI(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, organization_id, request_id):
        instance = get_object_or_404(ServiceRequest, id=request_id, organization_id=organization_id)
        serializer = ServiceRequestSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, organization_id, request_id):
        instance = get_object_or_404(ServiceRequest, id=request_id, organization_id=organization_id)
        serializer = ServiceRequestSerializer(
            instance,
            data=request.data,
            partial=True,
            context={"organization": instance.organization, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, organization_id, request_id):
        instance = get_object_or_404(ServiceRequest, id=request_id, organization_id=organization_id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
