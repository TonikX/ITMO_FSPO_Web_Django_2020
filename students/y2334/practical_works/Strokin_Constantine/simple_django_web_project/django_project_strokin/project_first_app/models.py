from django.db import models
import datetime

class Owner(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(("Date"), default=datetime.date.today)


class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    TYPE_ = (
        ('A','motorcycle'),
        ('B','car'),
        ('C','truck'),
        ('D','bus'),
    )
    number = models.IntegerField
    date_of_issue = models.DateField(("Date"), default=datetime.date.today)
    type = models.CharField(max_length=1,choices=TYPE_)




class Car(models.Model):
    mark = models.CharField(max_length=16)
    model = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    number = models.CharField(max_length=16)

class Possession(models.Model):
    owner = models.ForeignKey(Owner, on_delete = models.CASCADE)
    car = models.ForeignKey(Car,on_delete= models.CASCADE)
    date_of_start = models.DateField(("Date"), default=datetime.date.today)
    date_of_end = models.DateField(("Date"), default=datetime.date.today)