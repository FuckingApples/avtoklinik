from django.urls import path
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.documents.models import Product
from apps.api.serializers.documents import ProductSerializer


@extend_schema(tags=["Номенклатура"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание номенклатуры",
        request=ProductSerializer,
        responses={status.HTTP_201_CREATED: ProductSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех номенклатур организации",
        responses={status.HTTP_200_OK: ProductSerializer},
    ),
)
class OrganizationProductsAPI(BaseOrganizationModelView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@extend_schema(tags=["Номенклатура"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление номенклатуры",
        request=ProductSerializer,
        responses={status.HTTP_200_OK: ProductSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о номенклатуре",
        responses={status.HTTP_200_OK: ProductSerializer},
    ),
    delete=extend_schema(
        summary="Удаление номенклатуры",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class ProductsAPI(BaseOrganizationDetailView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


urlpatterns = [
    path(
        "",
        OrganizationProductsAPI.as_view(),
        name="organization_products",
    ),
    path(
        "<int:id>/",
        ProductsAPI.as_view(),
        name="products",
    ),
]
