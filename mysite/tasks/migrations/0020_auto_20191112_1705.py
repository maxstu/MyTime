# Generated by Django 2.2.6 on 2019-11-12 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_auto_20191112_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.TimeField(default=datetime.time(17, 5, 56, 148818), verbose_name='due time'),
        ),
    ]
