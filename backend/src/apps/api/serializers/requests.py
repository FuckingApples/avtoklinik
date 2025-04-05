from rest_framework import serializers
from apps.requests.models import ServiceRequest
from apps.deals.models import Deal
from apps.clients.models import Client
from apps.cars.models import Car

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = "__all__"

    def create(self, validated_data):
        organization = self.context["organization"]
        request = self.context["request"]

        if not validated_data.get("deal"):
            # Создание новой сделки, если не передана
            client = request.data.get("client")
            car = request.data.get("car")

            deal = Deal.objects.create(
                organization=organization,
                client_id=client,
                car_id=car,
                number=f"AUTO-{Deal.objects.filter(organization=organization).count() + 1}",
            )
            validated_data["deal"] = deal

        validated_data["organization"] = organization
        return super().create(validated_data)
