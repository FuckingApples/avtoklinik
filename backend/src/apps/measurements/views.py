from rest_framework import viewsets
from apps.measurements.models import MeasurementUnit
from apps.api.serializers.measurements import MeasurementUnitSerializer

class MeasurementUnitViewSet(viewsets.ModelViewSet):
    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer
