from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Patrolman(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    surname = models.CharField("Фамилия", max_length=30)
    name = models.CharField("Имя", max_length=30)
    position = models.CharField("Должность", max_length=40)
    begin_work = models.DateField("Дата начала работы", null=True)
    date_birth = models.DateField("Дата рождения", null=True)
    experience = models.IntegerField("Стаж", null=True)


class Patrol_result(models.Model):
    date_patrol = models.DateField("Дата патрулирования")
    vilorators_number = models.IntegerField("Количество нарушителей")


class Patrolman_has_patrol_result(models.Model):
    id_boat = models.IntegerField("Номер катера")
    service_number = models.ForeignKey(
        Patrolman,
        verbose_name="Номер патрульного",
        on_delete=models.SET_NULL,
        null=True)
    id_patrol_result = models.ForeignKey(
        Patrol_result,
        verbose_name="Номер патрулирования",
        on_delete=models.SET_NULL,
        null=True)


class Patrol_water_area(models.Model):
    water_area = models.IntegerField("Номер участка акватории")
    id_patrol_result = models.ForeignKey(
        Patrol_result,
        verbose_name="Номер патрулирования",
        on_delete=models.SET_NULL,
        null=True
    )
