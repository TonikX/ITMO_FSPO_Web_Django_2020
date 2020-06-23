from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Usr(AbstractUser):
    passport = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)

class Owner(models.Model):
    usr = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    owners = models.ManyToManyField(Owner, through='lesson3.Ownership')


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Car, on_delete=models.CASCADE)
    buying_Date = models.DateField()
    selling_Date = models.DateField()


class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    issueDate = models.DateField()
    type = models.CharField(max_length=50)
    number = models.IntegerField()