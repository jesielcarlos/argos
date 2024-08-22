from django.db import models
import uuid

class Project(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        verbose_name="Project Name",
        max_length=255
    )
    description = models.TextField(
        verbose_name="Project Description"
    )
    start_date = models.DateField(
        verbose_name="Project Start Date"
    )
    end_date = models.DateField(
        verbose_name="Project End Date"
    )