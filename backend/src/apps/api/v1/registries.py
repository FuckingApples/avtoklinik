from django.urls import path, include
from rest_framework import views, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.api.serializers.registries import CategorySerializer
from apps.organizations.models import Organization
from apps.registries.models import Category


class OrganizationCategoriesAPI(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, organization_id):
        get_object_or_404(Organization, id=organization_id)
        categories = Category.objects.filter(
            organization_id=organization_id, parent__isnull=True
        )
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, organization_id):
        organization = get_object_or_404(Organization, id=organization_id)
        serializer = CategorySerializer(
            data=request.data,
            context={"organization": organization, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoriesAPI(views.APIView):
    def get(self, request, organization_id, category_id):
        get_object_or_404(Organization, id=organization_id)
        category = Category.objects.filter(
            organization=organization_id, id=category_id
        ).first()
        serializer = CategorySerializer(category)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, organization_id, category_id):
        organization = get_object_or_404(Organization, id=organization_id)
        category = get_object_or_404(
            Category, id=category_id, organization=organization
        )
        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=True,
            context={"organization": organization, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, organization_id, category_id):
        organization = get_object_or_404(Organization, id=organization_id)
        category = get_object_or_404(
            Category, id=category_id, organization=organization
        )
        category.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


categories_urls = [
    path(
        "<int:organization_id>/",
        OrganizationCategoriesAPI.as_view(),
        name="organization_categories",
    ),
    path(
        "<int:organization_id>/<int:category_id>/",
        CategoriesAPI.as_view(),
        name="categories",
    ),
]

urlpatterns = [
    path("categories/", include(categories_urls)),
]
