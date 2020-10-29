from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model


class User(AbstractUser):
    passport = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)


class CarOwner(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthDate = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)


class Car(models.Model):
    carMark = models.CharField(max_length=10)
    model = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    carNumber = models.CharField(max_length=9)
    members = models.ManyToManyField(CarOwner, through='Ownership')


class DriversLicense(models.Model):
    CATEGORY = (
        ('A', 'Motorcycle'),
        ('B', 'Auto'),
        ('C', 'Truck'),
        ('D', 'Bus'),
        ('M', 'Moped'),
    )
    licenseNumber = models.IntegerField(primary_key=True, max_length=30)
    issueDate = models.DateField()
    type = models.CharField(max_length=10, choices=CATEGORY)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)


class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField(blank=True, null=True)
