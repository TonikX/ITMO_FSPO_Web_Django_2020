from django.db import models


class Train(models.Model):
    reg_number = models.CharField(max_length=6)
    departure = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date_time_departure = models.DateTimeField()
    date_time_destination = models.DateTimeField()


class Carriage(models.Model):
    reg_number_train = models.CharField(max_length=6)
    number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    number_of_seats = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)


class Seat(models.Model):
    id_carriage = models.CharField(max_length=50)
    number = models.IntegerField()
    status = models.CharField(max_length=50)


class Ticket(models.Model):
    name = models.CharField(max_length=50)
    number_passport = models.IntegerField()
    reg_number = models.CharField(max_length=6)
    departure = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date_time_departure = models.DateTimeField()
    date_time_destination = models.DateTimeField()
    number_carriage = models.IntegerField(default=0)
    number_seats = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
# Create your models here.
