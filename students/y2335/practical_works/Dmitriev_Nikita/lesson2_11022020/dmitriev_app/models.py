from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class Car(models.Model):
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    state_number = models.CharField(max_length=9)
    color = models.CharField(max_length=20)


class Owner_Addition(AbstractUser):
    passport_number = models.CharField(max_length=10, null=True, blank=True)
    home_address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=15, null=True, blank=True)


class Owner(models.Model):
    addition = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=20)
    secondName = models.CharField(max_length=30)
    birthday = models.DateField()
    cars = models.ManyToManyField(Car, through='Have')


class DriverLic(models.Model):
    num = models.IntegerField
    dateIssued = models.DateField
    TYPE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )
    type = models.CharField(max_length=1, choices=TYPE)
    driver = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Have(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    dateStart = models.DateField()
    dateEnd = models.DateField()
