from django.db import models


class Owner (models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_date = models.DateField()


class DriverLicense (models.Model):
    TYPE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    )
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.IntegerField()
    date = models.DateField()
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)


class Car (models.Model):
    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    state_number = models.CharField(max_length=10)

    def __str__(self):
        return self.mark


class Ownership (models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    begin_date = models.DateField()
    end = models.DateField()
