# Generated by Django 3.0.3 on 2020-06-05 19:17

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fuel_type', models.CharField(choices=[(1, 'Бензин'), (2, 'Дизельное топливо'), (3, 'Природный газ'), (4, 'Электриество')], max_length=100)),
                ('metric', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FuelInStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FuelProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('balance', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('img', models.ImageField(upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fuel_in_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.FuelInStation')),
            ],
        ),
        migrations.CreateModel(
            name='FuelStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('fuels', models.ManyToManyField(through='Core.FuelInStation', to='Core.Fuel')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.FuelProvider')),
            ],
        ),
        migrations.AddField(
            model_name='fuelinstation',
            name='clients',
            field=models.ManyToManyField(through='Core.Purchase', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fuelinstation',
            name='fuel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Fuel'),
        ),
        migrations.AddField(
            model_name='fuelinstation',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.FuelStation'),
        ),
    ]
