# Generated by Django 2.2.6 on 2019-11-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20191111_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(verbose_name='due date'),
        ),
    ]
