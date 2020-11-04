from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Расширенная модель пользователя
class User(AbstractUser):
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    card = models.CharField(max_length=20, default=None, blank=True, null=True)
    email = models.CharField(max_length=50)

# Модель производителя
class Fabric(models.Model):
    address = models.CharField(max_length=500)
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=50)

# Модель продукта
class Product(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=50)
    vendor_code = models.CharField(max_length=50)
    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE)
    image = models.CharField(max_length=300)

# Модель поставки
class Delivery(models.Model):
    delivery_date = models.DateField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_for_sale = models.FloatField()

# Модель продаж
class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
