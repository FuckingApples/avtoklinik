from django.urls import path, include

from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.core.views.base import BaseOrganizationModelView, BaseOrganizationDetailView
from apps.warehouses.models import Warehouse, Product, ProductStock
from apps.api.serializers.warehouses import (
    WarehouseSerializer,
    ProductSerializer,
    ProductStockSerializer,
)


@extend_schema(tags=["Склады"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание склада",
        request=WarehouseSerializer,
        responses={status.HTTP_201_CREATED: WarehouseSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех складов организации",
        responses={status.HTTP_200_OK: WarehouseSerializer},
    ),
)
class OrganizationWarehousesAPI(BaseOrganizationModelView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


@extend_schema(tags=["Склады"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление склада",
        request=WarehouseSerializer,
        responses={status.HTTP_200_OK: WarehouseSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о складе",
        responses={status.HTTP_200_OK: WarehouseSerializer},
    ),
    delete=extend_schema(
        summary="Удаление склада",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class WarehousesAPI(BaseOrganizationDetailView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


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


@extend_schema(tags=["Складские товары"])
@extend_schema_view(
    post=extend_schema(
        summary="Создание товара на складе",
        request=ProductStockSerializer,
        responses={status.HTTP_201_CREATED: ProductStockSerializer},
    ),
    get=extend_schema(
        summary="Получение списка всех складских товаров организации",
        responses={status.HTTP_200_OK: ProductStockSerializer},
    ),
)
class OrganizationProductStocksAPI(BaseOrganizationModelView):
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer


@extend_schema(tags=["Складские товары"])
@extend_schema_view(
    patch=extend_schema(
        summary="Обновление товара на складе",
        request=ProductStockSerializer,
        responses={status.HTTP_200_OK: ProductStockSerializer},
    ),
    get=extend_schema(
        summary="Получение информации о товаре на складе",
        responses={status.HTTP_200_OK: ProductStockSerializer},
    ),
    delete=extend_schema(
        summary="Удаление товара на складе",
        responses={status.HTTP_204_NO_CONTENT: None},
    ),
)
class ProductStocksAPI(BaseOrganizationDetailView):
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer


warehouses_urls = [
    path(
        "",
        OrganizationWarehousesAPI.as_view(),
        name="organization_warehouses",
    ),
    path(
        "<int:id>/",
        WarehousesAPI.as_view(),
        name="warehouses",
    ),
]

products_urls = [
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

product_stocks_urls = [
    path(
        "",
        OrganizationProductStocksAPI.as_view(),
        name="organization_product_stocks",
    ),
    path(
        "<int:id>/",
        ProductStocksAPI.as_view(),
        name="product_stocks",
    ),
]

urlpatterns = [
    path("", include(warehouses_urls)),
    path("products/", include(products_urls)),
    path("product_stocks/", include(product_stocks_urls)),
]
