from rest_framework import generics
from apps.measurements.models import MeasurementUnit
from apps.api.serializers.measurements import MeasurementUnitSerializer


class MeasurementUnitListCreateView(generics.ListCreateAPIView):
    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer


class MeasurementUnitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer
