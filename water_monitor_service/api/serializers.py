from rest_framework import serializers
from .models import WaterMonitoring


class WaterMonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterMonitoring
        fields = '__all__'
