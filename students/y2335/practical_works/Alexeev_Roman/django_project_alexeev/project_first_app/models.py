from django.db import models

# Create your models here.

class Car(models.Model):
    model = models.CharField(max_length=30)
    mark_name = models.CharField(max_length=30)
    colour = models.CharField(max_length=30)
    number_plate = models.CharField(max_length=10)



class CarOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()

class Owning(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    beginning_date = models.DateField()
    end_date = models.DateField()


class DriverLicense(models.Model):
    license_number = models.IntegerField()
    license_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    issue_date = models.DateField()
    TYPE_LICENSE = (
        ('A', 'motorcycle'),
        ('B', 'car'),
        ('D', 'bus'),
        ('M', 'moped'),
    )
    type = models.CharField(max_length=1, choices=TYPE_LICENSE)