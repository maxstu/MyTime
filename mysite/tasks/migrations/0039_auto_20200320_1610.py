# Generated by Django 3.0.2 on 2020-03-20 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0038_auto_20200320_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completion_delta',
            field=models.DurationField(blank=True, null=True, verbose_name='completion delta'),
        ),
        migrations.AddField(
            model_name='task',
            name='estimate_accuracy',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='estimate accuracy'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.TimeField(default=datetime.time(16, 10, 11, 620141), verbose_name='due time'),
        ),
    ]
