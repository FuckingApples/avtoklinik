from rest_framework import serializers

from apps.core.mixins import UniqueFieldsValidatorMixin
from apps.warehouses.models import Warehouse


class WarehouseSerializer(UniqueFieldsValidatorMixin, serializers.ModelSerializer):
    unique_fields = ["name"]

    class Meta:
        model = Warehouse
        fields = ("id", "name", "comment", "is_trade")

    def create(self, validated_data):
        validated_data["organization"] = self.context["organization"]
        return super().create(validated_data)
