from django.urls import path
from rest_framework import views, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.api.serializers.deals import DealSerializer
from apps.deals.models import Deal
from apps.organizations.models import Organization


class OrganizationDealsAPI(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, organization_id):
        get_object_or_404(Organization, id=organization_id)
        deals = Deal.objects.filter(organization_id=organization_id)
        serializer = DealSerializer(deals, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, organization_id):
        organization = get_object_or_404(Organization, id=organization_id)
        serializer = DealSerializer(
            data=request.data,
            context={"organization": organization, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DealsAPI(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, organization_id, deal_id):
        get_object_or_404(Organization, id=organization_id)
        deal = Deal.objects.filter(organization_id=organization_id, id=deal_id).first()
        serializer = DealSerializer(deal)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, organization_id, deal_id):
        organization = get_object_or_404(Organization, id=organization_id)
        deal = get_object_or_404(Deal, id=deal_id, organization=organization)
        serializer = DealSerializer(
            deal,
            data=request.data,
            partial=True,
            context={"organization": organization, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, organization_id, deal_id):
        organization = get_object_or_404(Organization, id=organization_id)
        deal = get_object_or_404(Deal, id=deal_id, organization=organization)
        deal.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


urlpatterns = [
    path(
        "",
        OrganizationDealsAPI.as_view(),
        name="organization_deals",
    ),
    path(
        "<int:deal_id>/",
        DealsAPI.as_view(),
        name="deals",
    ),
]
