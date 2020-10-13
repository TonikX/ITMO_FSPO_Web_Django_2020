# Generated by Django 3.1.2 on 2020-10-12 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cruis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cruis_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Motorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motorship_id', models.IntegerField()),
                ('motorship_name', models.CharField(max_length=45)),
                ('motorship_date_start', models.DateField()),
                ('motorship_date_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MotorshipTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.IntegerField()),
                ('route_days', models.IntegerField()),
                ('rote_stops', models.IntegerField()),
                ('rote_begin', models.CharField(max_length=45)),
                ('rote_end', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TicketCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='Category', max_length=45)),
                ('category_id', models.IntegerField()),
                ('category_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_id', models.IntegerField()),
                ('tour_datetime', models.DateTimeField()),
                ('cruis', models.ManyToManyField(to='app.Cruis')),
                ('motorship', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.motorship')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.IntegerField()),
                ('user_id', models.IntegerField(default=0)),
                ('ownername', models.CharField(default=' ', max_length=45, verbose_name='Ваше имя')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.ticketcategory')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.tour')),
            ],
        ),
        migrations.CreateModel(
            name='Sailor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sailor_id', models.IntegerField()),
                ('sailor_name', models.CharField(max_length=45)),
                ('sailor_lastName', models.CharField(max_length=45)),
                ('team', models.ManyToManyField(to='app.MotorshipTeam')),
            ],
        ),
        migrations.AddField(
            model_name='motorship',
            name='team',
            field=models.ManyToManyField(to='app.MotorshipTeam'),
        ),
        migrations.CreateModel(
            name='CruisRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cruis', models.ManyToManyField(to='app.Cruis')),
                ('route', models.ManyToManyField(to='app.Route')),
            ],
        ),
    ]
