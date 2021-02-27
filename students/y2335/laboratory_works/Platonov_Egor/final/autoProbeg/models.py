from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Mark(models.Model):
    title = models.CharField("Название марки", max_length=40)

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"

    def __str__(self):
        return self.title


class Model(models.Model):
    title = models.CharField("Наименование модели", max_length=50)

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return self.title


class Transmission(models.Model):
    title = models.CharField("Тип коробки", max_length=50)

    class Meta:
        verbose_name = "Коробка передач"
        verbose_name_plural = "Коробки передач"

    def __str__(self):
        return self.title


class Gear(models.Model):
    title = models.CharField("Привод", max_length=50)

    class Meta:
        verbose_name = "Привод"
        verbose_name_plural = "Приводы"

    def __str__(self):
        return self.title


class Auto(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Продавец",
        on_delete=models.CASCADE)
    model = models.ForeignKey(Model,
                              verbose_name="Модель",
                              on_delete=models.SET_NULL,
                              null=True)
    mark = models.ForeignKey(Mark,
                             verbose_name="Марка",
                             on_delete=models.SET_NULL,
                             null=True)
    pub_date = models.DateTimeField("Дата создания объявления", auto_now_add=True)
    transmission = models.ForeignKey(Transmission,
                                     verbose_name="Коробка передач",
                                     on_delete=models.SET_NULL,
                                     null=True)
    issue = models.IntegerField("Год выпуска")
    mileage = models.IntegerField("Пробег")
    color = models.CharField("Цвет", max_length=50)
    gear = models.ForeignKey(Gear,
                             verbose_name="Привод",
                             on_delete=models.SET_NULL,
                             null=True)
    engine = models.CharField("Двигатель", max_length=200)
    description = models.TextField("Описание")
    price = models.FloatField("Цена", null=True)
    count_owners = models.IntegerField("Количество владельцев")
    moderation = models.BooleanField("Модерация", default=False)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return "{} {} {}".format(self.user, self.mark, self.model)


