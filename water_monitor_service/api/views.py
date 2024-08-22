# views.py
from rest_framework import viewsets
from .models import WaterMonitoring
from .serializers import WaterMonitoringSerializer

class WaterMonitoringViewSet(viewsets.ModelViewSet):
    queryset = WaterMonitoring.objects.all()
    serializer_class = WaterMonitoringSerializer
