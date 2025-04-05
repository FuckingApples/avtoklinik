from rest_framework import serializers

from apps.cars.models import Car
from apps.clients.models import Client
from apps.deals.models import Deal


class DealSerializer(serializers.ModelSerializer):
    number = serializers.CharField()
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.none())
    car = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.none(),
        allow_null=True,
        required=False,
    )
    comment = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Deal
        fields = ("id", "number", "client", "car", "comment")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        organization = self.context.get("organization")

        if organization and self.context["request"].method in ["POST", "PUT", "PATCH"]:
            self.fields["client"].queryset = Client.objects.filter(
                organization=organization
            )
            self.fields["car"].queryset = Car.objects.filter(organization=organization)

    def validate_number(self, value):
        organization = self.context.get("organization")
        queryset = Deal.objects.filter(organization=organization, number=value)

        if queryset.exists():
            raise serializers.ValidationError(
                {
                    "message": "A deal with this number already exists.",
                    "code": "deal_number_already_exists",
                }
            )
        return value

    def create(self, validated_data):
        validated_data["organization"] = self.context["organization"]
        return super().create(validated_data)
