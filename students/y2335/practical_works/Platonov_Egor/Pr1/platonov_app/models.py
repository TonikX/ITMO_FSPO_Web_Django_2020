from django.db import models


class auto(models.Model):
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    date = models.DateField()


class users(models.Model):
    firstName = models.CharField(max_length=30)
    secondName = models.CharField(max_length=30)
    gend_choice = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, choices=gend_choice)
    driver = models.ManyToManyField(auto, through='Drivers')


class Drivers(models.Model):
    users = models.ForeignKey(users, on_delete=models.CASCADE)
    auto = models.ForeignKey(auto, on_delete=models.CASCADE)
    date_buy = models.DateField()
    date_Sell = models.DateField()


class drive_lic(models.Model):
    numb = models.CharField(max_length=10)
    type_choice = (
        ('RF', 'Russia'),
        ('I', 'International')
    )
    type = models.CharField(max_length=2, choices=type_choice)
    date_get = models.DateField()
    date_end = models.DateField()
    driver = models.ForeignKey(users, on_delete=models.CASCADE)
