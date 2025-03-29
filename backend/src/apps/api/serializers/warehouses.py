from dataclasses import dataclass

from rest_framework import serializers
from apps.warehouses.models import Warehouse


@dataclass
class WarehouseDTO:
    id: int
    name: str
    comment: str = None
    is_trade: bool = False

    @classmethod
    def from_instance(cls, warehouse: "Warehouse") -> "WarehouseDTO":
        return cls(
            id=warehouse.id,
            name=warehouse.name,
            comment=warehouse.comment,
            is_trade=warehouse.is_trade,
        )


class WarehouseSerializer(serializers.ModelSerializer):
    def validate(self, data):
        organization = data.get("organization")
        name = data.get("name")
        qs = Warehouse.objects.filter(organization=organization, name=name)

        if qs.exists():
            raise serializers.ValidationError(
                {
                    "message": "A warehouse with this name already exists.",
                    "code": "warehouse_already_exists",
                }
            )
        return data

    class Meta:
        model = Warehouse
        fields = ("id", "organization", "name", "comment", "is_trade")
