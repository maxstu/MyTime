# Generated by Django 3.0.2 on 2020-03-08 16:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0031_auto_20200308_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completion_time',
            field=models.DateTimeField(blank=True, verbose_name='completion time'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.TimeField(default=datetime.time(16, 12, 16, 875607), verbose_name='due time'),
        ),
    ]