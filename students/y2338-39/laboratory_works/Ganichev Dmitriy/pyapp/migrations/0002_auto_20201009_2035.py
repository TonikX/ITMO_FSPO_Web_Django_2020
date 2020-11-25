# Generated by Django 3.0.10 on 2020-10-09 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pyapp', '0001_initial'),
    ]

    def generate_su(apps, schema_editor):
        from django.contrib.auth.models import User
        su = User.objects.create_superuser(
            username="root",
            password="root",
            email="dev@null.no"
        )
        su.save()

        from pyapp.models import AppUser
        AppUser(user=User.objects.get(username="root"), role="A").save()

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('A', 'Admin'), ('H', 'Hunter'), ('W', 'FurPointWorker'), ('F', 'FurFactoryManager')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FurDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=45)),
                ('sort', models.IntegerField()),
                ('count', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FurFactory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='FurPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Hunter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=63)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyapp.AppUser')),
            ],
        ),
        migrations.CreateModel(
            name='FurShipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=45)),
                ('sort', models.IntegerField()),
                ('count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('id_furfactory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyapp.FurFactory')),
                ('id_furpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyapp.FurPoint')),
            ],
        ),
        migrations.AddField(
            model_name='furpoint',
            name='member',
            field=models.ManyToManyField(through='pyapp.FurDelivery', to='pyapp.Hunter'),
        ),
        migrations.AddField(
            model_name='furpoint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyapp.AppUser'),
        ),
        migrations.AddField(
            model_name='furfactory',
            name='member',
            field=models.ManyToManyField(through='pyapp.FurShipment', to='pyapp.FurPoint'),
        ),
        migrations.AddField(
            model_name='furfactory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyapp.AppUser'),
        ),
        migrations.AddField(
            model_name='furdelivery',
            name='id_furpoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyapp.FurPoint'),
        ),
        migrations.AddField(
            model_name='furdelivery',
            name='id_hunter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyapp.Hunter'),
        ),
        migrations.RunPython(generate_su)
    ]
