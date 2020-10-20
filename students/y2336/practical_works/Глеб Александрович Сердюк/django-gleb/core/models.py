from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ClientUser(AbstractUser):
    image = models.ImageField(upload_to='pic_users', default='default.jpg')
    phone_number = models.CharField(max_length=20)


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Jewelry(models.Model):
    image = models.ImageField(upload_to='pic_jewelry')
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()
    number = models.IntegerField()
    country = models.CharField(max_length=50)
    weight = models.FloatField()

    def __str__(self):
        return self.name


class Sale(models.Model):
    product = models.OneToOneField(Jewelry, on_delete=models.CASCADE)
    sale_percent = models.IntegerField()
    date_start = models.DateField()
    date_end = models.DateField()


class ProductInShoppingBag(models.Model):
    product = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    date_of_adding = models.DateTimeField(auto_now=True)


class Purchase(models.Model):
    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    date_of_purchase = models.DateTimeField()
    total_price = models.IntegerField()

    def __str__(self):
        return str(self.date_of_purchase).split('.')[0] + ' ' + str(self.total_price) + 'руб.'


class ProductInPurchase(models.Model):
    product = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
