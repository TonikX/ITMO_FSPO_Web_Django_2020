# Generated by Django 3.0.8 on 2020-07-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turist', '0008_trips'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='slug',
            field=models.SlugField(default=1, max_length=15, unique=True),
        ),
    ]
