# Generated by Django 3.0.10 on 2020-10-06 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour_buro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='completed_trip',
            old_name='route_name',
            new_name='route_id',
        ),
    ]