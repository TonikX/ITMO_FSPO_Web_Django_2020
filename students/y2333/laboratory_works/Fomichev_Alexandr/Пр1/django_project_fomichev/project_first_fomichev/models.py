from django.db import models

# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birthday = models.DateField()

class Auto(models.Model):
    mark = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    number = models.CharField(max_length=40)
    owners = models.ManyToManyField(Owner, through='Owning')


class Owning(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    buying_Date = models.DateField()
    selling_Date = models.DateField()


class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    issueDate = models.DateField()
    type = models.CharField(max_length=40)
    number = models.IntegerField()
