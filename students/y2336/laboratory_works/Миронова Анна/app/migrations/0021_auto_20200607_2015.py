# Generated by Django 3.0.6 on 2020-06-07 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200607_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='id_crew_member_1',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, related_name='crew_member_1', to='app.crew_member'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='id_crew_member_2',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, related_name='crew_member_2', to='app.crew_member'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='id_crew_member_3',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, related_name='crew_member_3', to='app.crew_member'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='id_flight',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='app.flight_information'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='id_helicopter',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='app.helicopter'),
        ),
    ]
