# Generated by Django 3.0.5 on 2020-04-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0002_auto_20200402_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverslicense',
            name='type',
            field=models.CharField(choices=[('A', 'Motorcycle'), ('B', 'Auto'), ('C', 'Truck'), ('D', 'Bus'), ('M', 'Moped')], max_length=10),
        ),
    ]
