# models.py
from django.db import models
import uuid

class WaterMonitoring(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    location = models.CharField(
        verbose_name="Location",
        max_length=255
    )
    level = models.FloatField(
        verbose_name="Water Level"
    )
    report_date = models.DateField(
        verbose_name="Report Date"
    )
