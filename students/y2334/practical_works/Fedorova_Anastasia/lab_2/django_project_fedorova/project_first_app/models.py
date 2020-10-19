from django.db import models


# Create your models here.
def __str__(self):
    return self.title


class Vehicle(models.Model):
    veh_brand = models.CharField(max_length=88)
    veh_model = models.CharField(max_length=88)
    veh_colour = models.CharField(max_length=88)
    veh_plate = models.CharField(max_length=8)


class Owner(models.Model):
    ow_first_name = models.CharField(max_length=88)
    ow_last_name = models.CharField(max_length=88)
    ow_dob = models.DateField()


class License(models.Model):
    lic_no = models.CharField(max_length=10)
    lic_date = models.DateField()
    types = (
        ('A', 'A'),
        ('A1', 'A1'),
        ('B', 'B'),
        ('B1', 'B1'),
        ('BE', 'BE'),
        ('C', 'C'),
        ('C1', 'C1'),
        ('CE', 'CE'),
        ('C1E', 'C1E'),
        ('D', 'D'),
        ('D1', 'D1'),
        ('DE', 'DE'),
        ('D1E', 'D1E'),
        ('M', 'M'),
        ('Tm', 'Tm'),
        ('Tb', 'Tb')
    )
    lic_type = models.CharField(max_length=3, choices=types)
    lic_owner = models.ForeignKey('Owner', on_delete=models.CASCADE)


class Ownership(models.Model):
    ship_owner = models.ManyToManyField('Owner')
    ship_vehicle = models.ManyToManyField('Vehicle')
    ship_open = models.DateField()
    ship_close = models.DateField()
