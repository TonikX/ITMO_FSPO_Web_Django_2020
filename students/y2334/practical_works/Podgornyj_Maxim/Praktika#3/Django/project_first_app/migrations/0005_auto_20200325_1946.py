# Generated by Django 3.0.4 on 2020-03-25 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0004_auto_20200325_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='Car',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='driverlicense',
            old_name='Name',
            new_name='IdPerson',
        ),
    ]
