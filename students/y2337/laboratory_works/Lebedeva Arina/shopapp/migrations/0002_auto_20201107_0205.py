# Generated by Django 3.1.3 on 2020-11-06 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='developer_has_book',
            new_name='developer_has_game',
        ),
    ]