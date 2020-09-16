from django.db import models

class Driver(models.Model):
    fio_driver = models.CharField("ФИО водителя", max_length=100)
    birthday = models.DateField("Дата рождения")
    phone = models.CharField("Телефон", max_length=12)
    license_number = models.IntegerField("Водительское удостоверение", max_length=10, unique=True)
    address = models.CharField("Адрес", max_length=45)

class Car(models.Model):
    brand = models.CharField("Марка", max_length=45)
    model = models.CharField("Модель", max_length=45)
    color = models.CharField("Цвет", max_length=45)
    pub_year = models.DateField("Год выпуска", max_length=4)
    date_reg = models.DateField("Дата регистрации")
    license_plate = models.CharField("Номер", max_length=6)
    driver = models.ManyToManyField(Driver, verbose_name="Водитель")

class Offence(models.Model):
    type = models.CharField("Нарушение", max_length=150)
    fine = models.IntegerField("Штраф")
    term_deprivation = models.IntegerField("Срок лишения прав")

class Inspector(models.Model):
    fio_inspector = models.CharField("ФИО инспектора", max_length=100)
    num_inspector = models.CharField("Номер сотрудника", max_length=10, unique=True)

class Judgement(models.Model):
    car = models.ManyToManyField(Car, verbose_name="Автомобиль")
    offence = models.ManyToManyField(Offence, verbose_name="Нарушение")
    date_judgement = models.DateField("Дата нарушения")
    time_judgement = models.TimeField("Время нарушения")
    area = models.CharField("Район", max_length=45)
    inspector = models.ManyToManyField(Inspector, verbose_name="Инспектор")

