from django.db import models


class Deliver(models.Model):
    id_deliver = models.IntegerField(primary_key=True, unique=True)
    date_of_acceptance = models.DateField()
    date_of_execution = models.DateField()


class Flower(models.Model):
    flower_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=40)
    sort = models.CharField(max_length=40)
    cost = models.IntegerField()


class Contract(models.Model):
    id_contract = models.IntegerField(primary_key=True, unique=True)
    id_deliver = models.ForeignKey(Deliver, blank=False, null=False, on_delete=models.CASCADE)


class Composition(models.Model):
    composition_id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=40)
    flower_id = models.ManyToManyField(Flower)
    id_contract = models.ForeignKey(Contract, blank=False, null=False, on_delete=models.CASCADE)

# Create your models here.
