from django.db import models

class Driver(models.Model):
    fio_driver = models.CharField("ФИО водителя", max_length=100)
    birthday = models.DateField("Дата рождения")
    phone = models.CharField("Телефон", max_length=12)
    license_number = models.IntegerField("Водительское удостоверение", max_length=10, unique=True)
    address = models.CharField("Адрес", max_length=45)

    def __str__(self):
        return self.fio_driver

class Car(models.Model):
    brand = models.CharField("Марка", max_length=45)
    model = models.CharField("Модель", max_length=45)
    color = models.CharField("Цвет", max_length=45)
    pub_year = models.DateField("Год выпуска", max_length=4)
    date_reg = models.DateField("Дата регистрации")
    license_plate = models.CharField("Номер", max_length=6)
    driver = models.ManyToManyField(Driver, verbose_name="Водитель", related_name="driver")

    def __str__(self):
        return self.license_plate

class Offence(models.Model):
    type = models.CharField("Нарушение", max_length=150)
    fine = models.IntegerField("Штраф")
    term_deprivation = models.IntegerField("Срок лишения прав")

    def __str__(self):
        return self.type

class Inspector(models.Model):
    fio_inspector = models.CharField("ФИО инспектора", max_length=100)
    num_inspector = models.CharField("Номер сотрудника", max_length=10, unique=True)

    def __str__(self):
        return self.fio_inspector

class Judgement(models.Model):
    objects = None
    DoesNotExist = None
    car = models.ManyToManyField(Car, verbose_name="Автомобиль", related_name="car")
    offence = models.ManyToManyField(Offence, verbose_name="Нарушение", related_name="offence")
    date_judgement = models.DateField("Дата нарушения")
    time_judgement = models.TimeField("Время нарушения")
    area = models.CharField("Район", max_length=45)
    inspector = models.ManyToManyField(Inspector, verbose_name="Инспектор", related_name="inspector")

    def __str__(self):
        return self.date_judgement

