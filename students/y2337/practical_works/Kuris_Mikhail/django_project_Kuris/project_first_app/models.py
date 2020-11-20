from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    passport = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=60, blank=True)
    nationality = models.CharField(max_length=20, blank=True)


class Owner (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class DriverLicense (models.Model):
    TYPE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    )
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.IntegerField()
    date = models.DateField()
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    def __str__(self):
        return self.number


class Car (models.Model):
    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    state_number = models.CharField(max_length=10)

    def __str__(self):
        return self.mark


class Ownership (models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    begin_date = models.DateField()
    end = models.DateField()