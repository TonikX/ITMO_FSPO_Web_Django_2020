# Generated by Django 3.1.3 on 2020-11-06 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fair_title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=45)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sort', models.CharField(max_length=255)),
                ('variety', models.IntegerField()),
                ('prise', models.FloatField()),
                ('organizations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.organizations')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='project_first_app.items')),
                ('sell_variety', models.IntegerField()),
                ('sell_prise', models.FloatField()),
                ('buyer', models.CharField(choices=[('Оптовик', 'Оптовик'), ('Частное лицо', 'Частное лицо'), ('Учреждение', 'Учреждение')], max_length=255)),
                ('fair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.fair')),
                ('organizations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.organizations')),
            ],
        ),
    ]