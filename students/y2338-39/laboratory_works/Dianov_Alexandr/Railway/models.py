from django.db import models
from django.shortcuts import render
from django.utils.timezone import now
from django.shortcuts import reverse


# Create your models here.
class Schedule(models.Model):
    RideId = models.PositiveIntegerField(primary_key=True, unique=True)

    DepartureTime = models.DateTimeField(default=now, blank=True)
    ArrivalTime = models.DateTimeField(default=now, blank=True)

    StartAt = models.CharField(max_length=150, db_index=True)
    FinishAt = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return '{}'.format(self.RideId)


class Train(models.Model):
    Train_ID = models.PositiveIntegerField(primary_key=True, unique=True)
    TrainName = models.CharField(max_length=150, db_index=True)
    TrainType = models.CharField(max_length=150, db_index=True)
    carCount = models.IntegerField(db_index=True)
    ScheduleID = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Train_ID)

# class Car(models.Model):

