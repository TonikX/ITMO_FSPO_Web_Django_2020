from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model




class Car(models.Model):
    mark = models.CharField(max_length=30)
    owner_surname = models.CharField(max_length=50)
    owner_address = models.CharField(max_length=150)
    number = models.CharField(max_length=9)
    date_of_issue = models.DateField()

class Workshop(models.Model):
    address = models.CharField(max_length=50)


class Master(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

class Type(models.Model):
    cost = models.CharField (max_length=6)
    name = models.CharField (max_length=50)

class Repair (models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    receipt_date = models.DateField()
    completion_date = models.DateField()
    repair_type = models.ForeignKey(Type, on_delete=models.CASCADE)


