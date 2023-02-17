# Generated by Django 3.0.7 on 2020-10-13 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201013_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='people',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
