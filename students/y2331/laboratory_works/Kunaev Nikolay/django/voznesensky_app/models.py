from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (
    ("М", "Мужской"),
    ("Ж", "Женский"),
    ("Д", "Другой")
)


class Client(models.Model):
    passport_id = models.CharField("Серия и номер паспорта", max_length=10)
    full_name = models.CharField("ФИО", max_length=64)
    birth_date = models.DateField("Дата рождения")
    address_registration = models.CharField("Адрес регистрации", max_length=256)
    address_residence = models.CharField("Адрес проживания", max_length=256)
    occupation = models.CharField("Профессия", max_length=45)
    phones = models.CharField("Телефоны", max_length=60)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=32, default="М")
    birth_place = models.CharField("Место рождения", max_length=45, blank=True)
    is_archived = models.BooleanField("Статус архивации", default=False)
    archived_reason = models.CharField("Причина архивации", max_length=60, blank=True)
    discovery_info = models.CharField("Откуда узнал", max_length=256, blank=True)
    email = models.CharField("Адрес электронной почты", max_length=60, blank=True)
    comment = models.CharField("Комментарий", max_length=256, blank=True)
    comment_addition = models.CharField("Дополнительный комментарий", max_length=256, blank=True)
    balance = models.IntegerField("Баланс", default=0)
    permanent_discount = models.IntegerField("Постоянная скидка", default=0)

    def __str__(self):
        return self.full_name


class DiscountCard(models.Model):
    percent = models.IntegerField("Размер скидки (%)")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class Transaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    change = models.IntegerField("Объём")
    date_time = models.DateTimeField()
    comment = models.CharField("Комментарий", max_length=64)

    def __str__(self):
        return f'{self.change} {self.client} {self.date_time} {self.comment}'


class Item(models.Model):
    qty = models.IntegerField("Количество")
    price = models.IntegerField("Цена")
    name = models.CharField("Наименование", max_length=128)
    group = models.CharField("Группа", max_length=128)

    def __str__(self):
        return self.name


class SoldItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price_actual = models.IntegerField("Общая цена")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField("Дата продажи")
    isDiscountCardUsed = models.BooleanField("Предъявлена скидочная карта")


VISIT_STATUS_CHOICES = (
    ('не пришел', 'Еще не пришел'),
    ('пришел', 'Пришел на прием, еще не в кресле'),
    ('в кресле', 'В кресле у врача'),
    ('отменен', 'Посещение отменено'),
)


class Visit(models.Model):
    date = models.DateTimeField("Дата визита")
    isFirst = models.IntegerField()
    reason = models.CharField("Причина", max_length=256)
    comment = models.CharField("Комментарий", max_length=256)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    isDiscountCardUsed = models.IntegerField()
    status = models.CharField(choices=VISIT_STATUS_CHOICES, max_length=32)
