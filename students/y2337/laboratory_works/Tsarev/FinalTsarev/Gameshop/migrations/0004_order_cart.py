# Generated by Django 3.1.1 on 2020-10-06 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gameshop', '0003_auto_20201006_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gameshop.cart', verbose_name='Корзина'),
        ),
    ]
