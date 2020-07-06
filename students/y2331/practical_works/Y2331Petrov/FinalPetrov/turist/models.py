from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Bus(models.Model):
    BusNum = models.IntegerField(unique=True)
    NameB = models.CharField(max_length=15)
    Mileage = models.IntegerField()


class Route(models.Model):
    Name = models.CharField(max_length=30, unique=True)
    StartP = models.CharField(max_length=45)
    EndP = models.CharField(max_length=45)
    Length = models.IntegerField()


class Crew(models.Model):
    Surname = models.CharField(max_length=15)
    Number = models.IntegerField(unique=True)
    Exp = models.CharField(max_length=45)
    Category = models.CharField(max_length=1)
    Address = models.CharField(max_length=45)
    Birthday = models.DateField()
    FkBusNum = models.ForeignKey(Bus, on_delete=models.CASCADE)


class Trips(models.Model):
    slug = models.SlugField(max_length=15, unique=True, default=1)
    DateS = models.DateField()
    DateE = models.DateField()
    Qty = models.IntegerField()
    Price = models.IntegerField()
    FkBusNum = models.ForeignKey(Bus, on_delete=models.CASCADE)
    FkRoute = models.ForeignKey(Route, on_delete=models.CASCADE)
    turi = models.CharField(max_length=15, default=' ')

    def get_absolute_url(self):
        return reverse('route_detail', kwargs={'slug': self.slug})

    def get_next_url(self):
        return reverse('zakaz', kwargs={'slug': self.slug})

