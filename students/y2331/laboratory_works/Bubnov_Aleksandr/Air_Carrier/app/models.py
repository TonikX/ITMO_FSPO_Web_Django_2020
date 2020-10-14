from django.db import models
from django.contrib.auth.models import User


class Heli(models.Model):
    heli_id = models.IntegerField()
    mark = models.CharField(max_length=50)
    prod_date = models.DateField()

    object = models.Manager()


class Crew(models.Model):
    crew_id = models.IntegerField()

    object = models.Manager()


class Pilot(models.Model):
    pilot_id = models.IntegerField()
    surname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    birthdate = models.DateField()
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)

    object = models.Manager()


class Flight(models.Model):
    flight_id = models.IntegerField()
    flight_date = models.DateField()
    duration = models.IntegerField()
    heli = models.ForeignKey(Heli, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    object = models.Manager()


class Ticket(models.Model):
    CHOISES = [
        ('Lux', 'Lux'),
        ('Normal', 'Normal'),
        ('Budget', 'Budget')
    ]
    ticket_id = models.IntegerField()
    user_id = models.IntegerField(default=0)
    category = models.CharField(max_length=50, choices=CHOISES)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
