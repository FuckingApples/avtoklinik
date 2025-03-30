from rest_framework import serializers
from .models import MeasurementUnit

class MeasurementUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementUnit
        fields = '__all__'
