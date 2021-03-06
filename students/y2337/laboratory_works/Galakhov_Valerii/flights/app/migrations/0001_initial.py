# Generated by Django 3.1.3 on 2020-11-03 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Helicopter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название модели')),
                ('carryingCapacity', models.FloatField(verbose_name='Максимальная грузоподъёмность, т')),
                ('dateOfProduction', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pilotName', models.CharField(max_length=30, verbose_name='Имя пилота')),
                ('pilotPost', models.CharField(max_length=30, verbose_name='Должность')),
                ('pilotExperience', models.PositiveIntegerField(verbose_name='Стаж')),
                ('dateOfBirth', models.DateField()),
                ('idHelicopter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.helicopter', verbose_name='Вертолёт')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfFlight', models.DateField()),
                ('cargoWeight', models.PositiveIntegerField(verbose_name='Масса перевезённого груза, т')),
                ('flightDuration', models.PositiveIntegerField(verbose_name='Длительность рейса, ч')),
                ('flightCost', models.PositiveIntegerField(verbose_name='Стоимость рейса')),
                ('idHelicopter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.helicopter', verbose_name='Вертолёт')),
            ],
        ),
    ]
