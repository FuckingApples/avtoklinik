from rest_framework import serializers

from apps.core.mixins import UniqueFieldsValidatorMixin
from apps.core.serializers import BaseOrganizationModelSerializer
from apps.warehouses.models import Warehouse


class WarehouseSerializer(UniqueFieldsValidatorMixin, BaseOrganizationModelSerializer):
    unique_fields = ["name"]

    class Meta:
        model = Warehouse
        fields = ("id", "name", "comment", "is_trade")
