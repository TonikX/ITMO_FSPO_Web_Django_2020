# Generated by Django 3.0.7 on 2020-06-29 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comppubhouse_app', '0007_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='score',
            field=models.DecimalField(decimal_places=0, default=10, max_digits=2),
        ),
    ]
