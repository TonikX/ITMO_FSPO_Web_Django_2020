# Generated by Django 3.1.2 on 2020-10-06 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_productinshoppingbag_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jewelry',
            name='description',
        ),
    ]
