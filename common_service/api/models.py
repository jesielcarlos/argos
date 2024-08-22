# models.py
from django.db import models
import uuid

class KPI(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    related_entity_id = models.UUIDField(
        verbose_name="Related Entity ID"
    )
    # Ex: "ConstructionService" ou "WaterMonitoringService"
    related_entity_service = models.CharField(
        verbose_name="Related Entity Service",
        max_length=100
    )
    metric_name = models.CharField(
        verbose_name="Metric Name",
        max_length=255
    )
    metric_value = models.FloatField(
        verbose_name="Metric Value"
    )
    timestamp = models.DateTimeField(
        verbose_name="Timestamp",
        auto_now_add=True
    )
