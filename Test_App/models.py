from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    passport = models.CharField(max_length=10)
    home_address = models.CharField(max_length=150)
    ethnic = models.CharField(max_length=30)

class Car(models.Model):
    Mark = models.CharField(max_length=25)
    Model = models.CharField(max_length=25)
    Color = models.CharField(max_length=25)
    Number = models.CharField(max_length=10)


class Owner(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    birthday = models.DateField
    car = models.ManyToManyField(Car, through='Vladenie')


class Vladenie(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()


class License(models.Model):
    TYPE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )
    License_num = models.IntegerField
    date_get = models.DateField
    License_type = models.CharField(max_length=1, choices=TYPE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
