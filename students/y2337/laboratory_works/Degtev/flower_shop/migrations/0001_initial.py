# Generated by Django 3.1.2 on 2020-10-13 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id_customer', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('capital', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('id_deliver', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('date_of_acceptance', models.DateField()),
                ('date_of_execution', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('flower_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('sort', models.CharField(max_length=40)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id_contract', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('id_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower_shop.customer')),
                ('id_deliver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower_shop.deliver')),
            ],
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('composition_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=40)),
                ('contract_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower_shop.contract')),
                ('flower_id', models.ManyToManyField(to='flower_shop.Flower')),
            ],
        ),
    ]
