# Generated by Django 3.0.7 on 2020-06-29 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comppubhouse_app', '0008_feedback_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
