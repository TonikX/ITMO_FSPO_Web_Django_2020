# Generated by Django 3.0.8 on 2020-07-02 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turist', '0005_auto_20200702_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trips',
            name='slug',
        ),
    ]
