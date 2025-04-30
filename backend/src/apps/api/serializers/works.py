from apps.core.mixins import UniqueFieldsValidatorMixin
from apps.core.serializers import (
    BaseOrganizationModelSerializer,
    OrgPrimaryKeyRelatedField,
)
from apps.registries.models import HourlyWage
from apps.warehouses.models import Product
from apps.works.models import Work


class WorkSerializer(
    UniqueFieldsValidatorMixin,
    BaseOrganizationModelSerializer,
):
    hourly_wage = OrgPrimaryKeyRelatedField(
        queryset=HourlyWage.objects.all(), allow_null=True, required=False
    )
    related_works = OrgPrimaryKeyRelatedField(
        queryset=Work.objects.all(), many=True, required=False
    )
    products = OrgPrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True, required=False
    )

    unique_fields = ["work_code", "barcode"]

    class Meta:
        model = Work
        fields = (
            "id",
            "name",
            "executor",
            "category",
            "price",
            "norm_time",
            "max_discount",
            "coefficient",
            "multiplicity",
            "comment",
            "barcode",
            "work_code",
            "hourly_wage",
            "related_works",
            "products",
        )
