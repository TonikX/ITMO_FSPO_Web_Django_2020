from django.db import models
from django.contrib.auth.models import User


class Cassette(models.Model):
    title = models.CharField(max_length=45, null=False)
    subjects = models.CharField(max_length=20, null=False)
    producer = models.CharField(max_length=45, null=False)
    price = models.DecimalField(max_digits=3, decimal_places=0, null=False)
    year_of_release = models.IntegerField(null=False)
    film_studio = models.CharField(max_length=45, null=False)
    count = models.DecimalField(max_digits=5, decimal_places=0, null=False, default=0)
    in_order = models.ManyToManyField('Order', through='CassetteInOrder')


class Seller(models.Model):
    first_name = models.CharField(max_length=10, null=False)
    last_name = models.CharField(max_length=20, null=False)


class Admission(models.Model):
    cassette = models.ForeignKey('Cassette', on_delete=models.CASCADE, null=False)
    count = models.DecimalField(max_digits=5, decimal_places=0, null=False, default=0)
    date = models.DateTimeField(auto_now=False, null=True)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE, null=False)


class Order(models.Model):
    customer = models.IntegerField(default=0, null=False)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now=False, null=True)
    bought = models.BooleanField(null=False, default=False)


class CassetteInOrder(models.Model):
    cassette = models.ForeignKey('Cassette', on_delete=models.CASCADE, null=False)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=False)
    count = models.DecimalField(max_digits=5, decimal_places=0, null=False, default=0)
    price = models.DecimalField(max_digits=3, decimal_places=0, null=False)
