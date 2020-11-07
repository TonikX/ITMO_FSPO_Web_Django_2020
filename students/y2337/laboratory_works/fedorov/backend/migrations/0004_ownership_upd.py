# Generated by Django 3.0.7 on 2020-06-30 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_intrip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='owner',
        ),
        migrations.AddField(
            model_name='appuser',
            name='cars',
            field=models.ManyToManyField(to='backend.Car'),
        ),
    ]
