# Generated by Django 2.2.6 on 2019-11-11 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_auto_20191111_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.TimeField(default=datetime.time(17, 52, 59, 967048), verbose_name='due time'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_estimate',
            field=models.DurationField(default=datetime.timedelta(0), verbose_name='time estimate'),
        ),
    ]