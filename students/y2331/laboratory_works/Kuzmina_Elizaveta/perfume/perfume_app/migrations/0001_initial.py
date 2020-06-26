# Generated by Django 3.0.7 on 2020-06-20 22:13

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
            name='Broker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=80)),
                ('birthdate', models.DateField()),
                ('broker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_deal', models.DateField()),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfume_app.Broker')),
            ],
        ),
        migrations.CreateModel(
            name='Fabricator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_fabricator', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=45)),
                ('legal_address', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_firm', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=45)),
                ('legal_address', models.CharField(max_length=80)),
                ('type_firm', models.CharField(choices=[('S', 'Seller'), ('B', 'Buyer')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('type', models.CharField(choices=[('PA', 'Parfum'), ('EP', 'Eau de Parfum'), ('ET', 'Eau de Toilette'), ('EC', 'Eau de Cologne'), ('EF', 'Eau Fraiche')], max_length=2)),
                ('shelf_life', models.IntegerField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unisex')], max_length=1)),
                ('fabricator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfume_app.Fabricator')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_sold', models.IntegerField()),
                ('cost_seller', models.DecimalField(decimal_places=2, max_digits=12)),
                ('cost_broker', models.DecimalField(decimal_places=2, max_digits=12)),
                ('deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfume_app.Deal')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfume_app.Product')),
            ],
        ),
        migrations.AddField(
            model_name='deal',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='perfume_app.Firm'),
        ),
        migrations.AddField(
            model_name='deal',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='perfume_app.Firm'),
        ),
    ]