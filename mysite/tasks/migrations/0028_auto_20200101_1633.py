# Generated by Django 3.0.1 on 2020-01-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0027_auto_20200101_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_time',
            field=models.TimeField(default='00:00', verbose_name='due time'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(verbose_name='due date'),
        ),
    ]
