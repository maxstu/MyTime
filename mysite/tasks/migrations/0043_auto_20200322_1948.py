# Generated by Django 3.0.2 on 2020-03-22 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0042_auto_20200322_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.TimeField(default=datetime.time(19, 48, 34, 491240), verbose_name='due time'),
        ),
    ]