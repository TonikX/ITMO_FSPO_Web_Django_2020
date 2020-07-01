from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from rest_framework.compat import MinValueValidator, MaxValueValidator


class Route(models.Model):
    routeName = models.TextField(verbose_name="Название маршрута")
    startCity = models.TextField(verbose_name="Город отправления")
    finishCity = models.TextField(verbose_name="Город прибытия")
    distance = models.DecimalField(verbose_name="Протяженность маршрута", decimal_places=2, max_digits=12)

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршруты"


class Bus(models.Model):
    LICENSE_TYPE = (
        ('D', "Bus"),
        ('DE', "Bus with trailer"),
        ('D1', "Small bus"),
        ('D1E', "Small bus with trailer")
    )
    busName = models.TextField(verbose_name="Название автобуса")
    mileage = models.PositiveIntegerField(verbose_name="Пробег")
    busType = models.CharField(max_length=3, verbose_name="Тип прав", choices=LICENSE_TYPE)
    busNumber = models.CharField(max_length=4, verbose_name="Номер автобуса", default="A111")

    class Meta:
        verbose_name = "Автобус"
        verbose_name_plural = "Автобусы"


class Race(models.Model):
    STATE_FOR_RACE = (
        ('R', "Ready"),
        ('D', "Done"),
        ('C', "Cancelled")
    )
    dateStart = models.DateField("Дата отправления", blank=True)
    dateFinish = models.DateField("Дата прибытия", blank=True)
    amount = models.PositiveIntegerField(verbose_name="Количество пассажиров", max_length=2)
    price = models.DecimalField(verbose_name="Цена билета", decimal_places=2, max_digits=12)
    state = models.CharField(max_length=1, verbose_name="Состояние", choices=STATE_FOR_RACE)
    raceRoute = models.ForeignKey(Route, verbose_name="Маршрут отправки", on_delete=models.CASCADE)
    raceBus = models.ForeignKey(Bus, verbose_name="Автобус маршрута", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    fullName = models.TextField(verbose_name="ФИО", blank=True)
    location = models.TextField(verbose_name="Адрес", blank=True)
    birth_date = models.DateField(verbose_name="Дата регистрации", auto_now_add=True, blank=True)
    position = models.CharField(verbose_name="Должность", blank=True, max_length=200)
    contacts = models.CharField(verbose_name="Контакты", blank=True, max_length=200)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class Drivers(models.Model):
    DRIVER_CATEGORY = (
        ('D', "Bus"),
        ('DE', "Bus with trailer"),
        ('D1', "Small bus"),
        ('D1E', "Small bus with trailer")
    )
    person = models.ForeignKey(Profile, verbose_name="Гражданин", on_delete=models.CASCADE)
    experience = models.PositiveIntegerField(verbose_name="Стаж")
    category = models.CharField(max_length=3, verbose_name="Категория", choices=DRIVER_CATEGORY)
    driverBus = models.ForeignKey(Bus, verbose_name="Автобус водителя", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()
