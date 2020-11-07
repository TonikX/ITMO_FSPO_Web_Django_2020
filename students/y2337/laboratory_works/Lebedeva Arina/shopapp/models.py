from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class Developer(models.Model):
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)


class Game(models.Model):
    name_game = models.CharField(max_length=45)
    genre = models.CharField(max_length=45)
    year = models.IntegerField()
    developer_has_game = models.ManyToManyField(Developer)
    price = models.FloatField(default=0)


class CD(models.Model):
    idcd = models.IntegerField()
    date = models.DateField()
    price = models.FloatField(default=0)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    login = models.CharField(max_length=45)
    id_customer = models.IntegerField()


class Order(models.Model):
    date = models.DateField()
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Game_has_Order = models.ManyToManyField(Game)