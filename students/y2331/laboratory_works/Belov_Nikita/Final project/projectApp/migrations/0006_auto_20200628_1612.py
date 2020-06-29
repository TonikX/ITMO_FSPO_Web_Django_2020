# Generated by Django 3.0.3 on 2020-06-28 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0005_auto_20200627_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fishoperation',
            name='optType',
        ),
        migrations.RemoveField(
            model_name='fishoperation',
            name='tId',
        ),
        migrations.AddField(
            model_name='fishoperation',
            name='date',
            field=models.DateField(default='1970-01-03'),
        ),
        migrations.AlterField(
            model_name='crews',
            name='uId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
