from apps.calculations.models import Calculation
from apps.core.mixins import UniqueFieldsValidatorMixin
from apps.core.serializers import (
    BaseOrganizationModelSerializer,
    OrgPrimaryKeyRelatedField,
)
from apps.clients.models import Client
from apps.cars.models import Car
from apps.deals.models import Deal
from apps.warehouses.models import ProductStock
from apps.works.models import Work

class CalculationSerializer(
    UniqueFieldsValidatorMixin,
    BaseOrganizationModelSerializer
):
    client = OrgPrimaryKeyRelatedField(
        queryset=Client.objects.none()
    )
    car = OrgPrimaryKeyRelatedField(
        queryset=Car.objects.none()
    )
    deal = OrgPrimaryKeyRelatedField(
        queryset=Deal.objects.all()
    )
    productStock = OrgPrimaryKeyRelatedField(
        queryset=ProductStock.objects.all(),
        allow_null = True,
        required = False,
    )
    works = OrgPrimaryKeyRelatedField(
        queryset=Work.objects.all(),
        many=True,
        required=False
    )
    organization_related_fields = {
        "client": Client,
        "car": Car,
        "deal": Deal,
        "productStock": ProductStock,
        "works": Work,
    }
    unique_fields = ["calculation_number"]

    class Meta:
        model = Calculation
        fields = (
            "id",
            "client",
            "name",
            "car",
            "responsible",
            "calculation_number",
            "deal",
            "special_notes",
            "productStock",
            "works",
            "commentary",
        )