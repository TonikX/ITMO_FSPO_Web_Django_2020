# Generated by Django 3.0.6 on 2020-06-07 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200606_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight_information',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
