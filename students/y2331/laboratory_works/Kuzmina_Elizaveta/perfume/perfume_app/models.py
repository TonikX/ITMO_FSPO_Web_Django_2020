from django.db import models
from django.contrib.auth.models import User


# from djoser.urls.base import User

class Broker(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    birthdate = models.DateField()
    broker = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)


class Firm(models.Model):
    TYPE_FIRM = [('S', 'Seller'), ('B', 'Buyer')]
    name_firm = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    legal_address = models.CharField(max_length=80)
    type_firm = models.CharField(max_length=1, choices=TYPE_FIRM)


class Deal(models.Model):
    date_deal = models.DateField()
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Firm, related_name='buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(Firm, related_name='seller', on_delete=models.CASCADE)


class Fabricator(models.Model):
    name_fabricator = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    legal_address = models.CharField(max_length=80)


class Product(models.Model):
    TYPE = [
        ('PA', 'Parfum'),
        ('EP', 'Eau de Parfum'),
        ('ET', 'Eau de Toilette'),
        ('EC', 'Eau de Cologne'),
        ('EF', 'Eau Fraiche')
    ]
    SEX = [('M', 'Male'), ('F', 'Female'), ('U', 'Unisex')]
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=2, choices=TYPE)
    shelf_life = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX)
    fabricator = models.ForeignKey(Fabricator, on_delete=models.CASCADE)


class OrderDeal(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_sold = models.IntegerField()
    cost_seller = models.DecimalField(max_digits=12, decimal_places=2)
    cost_broker = models.DecimalField(max_digits=12, decimal_places=2)