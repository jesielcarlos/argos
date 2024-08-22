from rest_framework import viewsets
from .models import KPI
from .serializers import KPISerializer

class KPIViewSet(viewsets.ModelViewSet):
    queryset = KPI.objects.all()
    serializer_class = KPISerializer
