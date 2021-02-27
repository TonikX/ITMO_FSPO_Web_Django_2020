# Generated by Django 3.1.1 on 2020-10-14 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Привод')),
            ],
            options={
                'verbose_name': 'Привод',
                'verbose_name_plural': 'Приводы',
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название марки')),
            ],
            options={
                'verbose_name': 'Марка',
                'verbose_name_plural': 'Марки',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование модели')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Тип коробки')),
            ],
            options={
                'verbose_name': 'Коробка передач',
                'verbose_name_plural': 'Коробки передач',
            },
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания объявления')),
                ('issue', models.IntegerField(verbose_name='Год выпуска')),
                ('mileage', models.IntegerField(verbose_name='Пробег')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('engine', models.CharField(max_length=200, verbose_name='Двигатель')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.FloatField(null=True, verbose_name='Цена')),
                ('count_owners', models.IntegerField(verbose_name='Количество владельцев')),
                ('moderation', models.BooleanField(default=False, verbose_name='Модерация')),
                ('gear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoProbeg.gear', verbose_name='Привод')),
                ('mark', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoProbeg.mark', verbose_name='Марка')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoProbeg.model', verbose_name='Модель')),
                ('transmission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoProbeg.transmission', verbose_name='Коробка передач')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]