# Generated by Django 3.0.2 on 2020-03-08 16:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0032_auto_20200308_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.TimeField(default=datetime.time(16, 12, 45, 683044), verbose_name='due time'),
        ),
    ]