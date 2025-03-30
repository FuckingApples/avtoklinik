from rest_framework import viewsets
from .models import MeasurementUnit
from .serializers import MeasurementUnitSerializer

class MeasurementUnitViewSet(viewsets.ModelViewSet):
    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer
