# Generated by Django 3.1.2 on 2020-10-25 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20201021_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='currentCusromer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=30)),
                ('passport', models.BigIntegerField()),
                ('phone', models.BigIntegerField()),
            ],
        ),
    ]
