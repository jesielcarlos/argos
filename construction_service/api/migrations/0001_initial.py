# Generated by Django 5.1 on 2024-08-22 01:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Project Name')),
                ('description', models.TextField(verbose_name='Project Description')),
                ('start_date', models.DateField(verbose_name='Project Start Date')),
                ('end_date', models.DateField(verbose_name='Project End Date')),
            ],
        ),
    ]
