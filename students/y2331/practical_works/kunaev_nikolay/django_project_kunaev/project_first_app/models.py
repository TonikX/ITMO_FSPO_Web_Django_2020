from django.db import models


# Create your models here.

class CarOwner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dateOfBirth = models.DateField()


class DriverDocument(models.Model):
    DOC_TYPE = (
        ('A', 'Motorcycle'),
        ('A1', 'Light motorcycle'),
        ('B', 'Light car, small truck'),
        ('BE', 'Car with trailer'),
        ('B1', 'Tricycle'),
        ('C', 'Truck'),
        ('CE', 'Truck with trailer'),
        ('C1', 'Medium truck'),
        ('C1E', 'Medium truck with trailer'),
        ('D', 'Bus'),
        ('DE', 'Bus with truck'),
        ('D1', 'Small bus'),
        ('D1E', 'Small bus with truck'),
        ('M', 'Moped'),
        ('Tm', 'Tram'),
        ('Tb', 'Trolleybus'))
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    date_of_issue = models.DateField()
    type = models.CharField(max_length=3, choices=DOC_TYPE)


class Car(models.Model):
    mark = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=15)
    state_number = models.PositiveIntegerField()


class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    state_number = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_the_beginning = models.DateField()
    date_of_expiration = models.DateField()
