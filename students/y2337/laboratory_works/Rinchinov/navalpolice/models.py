from django.db import models


# Create your models here.

class Boat(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, null=False, blank=False, default="")

    def __str__(self):
        return self.name


class Patrol(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50, blank=False)
    position = models.CharField(max_length=100)
    exp = models.IntegerField()
    age = models.IntegerField()
    boat_id = models.ForeignKey(Boat, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + "#" + self.name


class Patrolling(models.Model):
    date = models.DateField(blank=False)
    boat_id = models.ForeignKey(Boat, on_delete=models.CASCADE)
    area_id = models.IntegerField(blank=False)
    count = models.IntegerField()

    def __str__(self):
        return self.date + str(self.area_id)
