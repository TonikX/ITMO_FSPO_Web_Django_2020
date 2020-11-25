from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class AppUser(models.Model):
    USER_TYPE = (
        ('A', 'Admin'),
        ('H', 'Hunter'),
        ('W', 'FurPointWorker'),
        ('F', 'FurFactoryManager')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(blank=False, choices=USER_TYPE, max_length=1)


class Hunter(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=63)


class FurPoint(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=45)
    member = models.ManyToManyField(Hunter, through='FurDelivery')


class FurFactory(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    member = models.ManyToManyField(FurPoint, through='FurShipment')


class FurDelivery(models.Model):
    id_hunter = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    id_furpoint = models.ForeignKey(FurPoint, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    type = models.CharField(max_length=45)
    sort = models.IntegerField()
    count = models.IntegerField()
    price = models.IntegerField()


class FurShipment(models.Model):
    id_furfactory = models.ForeignKey(FurFactory, on_delete=models.CASCADE)
    id_furpoint = models.ForeignKey(FurPoint, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    type = models.CharField(max_length=45)
    sort = models.IntegerField()
    count = models.IntegerField()
    price = models.IntegerField()


class FurGathering(models.Model):
    id_hunter = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    type = models.CharField(max_length=45)
    sort = models.IntegerField()
    count = models.IntegerField()
