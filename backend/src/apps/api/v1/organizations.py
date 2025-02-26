from pyexpat.errors import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.api.serializers.organizations import OrganizationSerializer
from apps.organizations.models import Organization, PermissionFlags
from apps.organizations.permissions import HasPermissions
from apps.organizations.services import organizations
from apps.organizations.services.organizations import delete_organization


class CreateOrgAPI(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = organizations.create_organization(
            organization=data, user=request.user
        )

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class DeleteOrgAPI(APIView):
    permission_classes = [HasPermissions]
    required_permissions = PermissionFlags.OWNER

    def delete(self, request, organization_id):
        try:
            delete_organization(organization_id=organization_id)
        except Organization.DoesNotExist:
            return Response(
                {
                    "message": "Organization does not exist",
                    "code": "organization_does_not_exist",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
