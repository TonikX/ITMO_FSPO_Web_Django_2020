from django.db import models


class User(models.Model):
    SEX_DATA = (('M', 'Male'), ('F', 'Female'))
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=SEX_DATA)
    idNumber = models.CharField(max_length=30)
    def __str__(self):
        return self.idNumber


class Car(models.Model):
    carMake = models.CharField(max_length=30)
    carModel = models.CharField(max_length=30)
    prodYear = models.IntegerField()
    dates = models.ManyToManyField(User, through='CarUser')


class dLicense(models.Model):
    DL_DATA = (('F', 'Foreign'), ('N', 'Native'))
    dlNum = models.CharField(max_length=30)
    type = models.CharField(max_length=1, choices=DL_DATA)
    someKey = models.ForeignKey(User, on_delete=models.CASCADE)


class CarUser(models.Model):
    automobile_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    human_id = models.ForeignKey(User, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()


class SomeModel(models.Model):
    title = models.CharField(max_length = 255)
    descript = models.TextField()
    def __str__(self):
        return self.title