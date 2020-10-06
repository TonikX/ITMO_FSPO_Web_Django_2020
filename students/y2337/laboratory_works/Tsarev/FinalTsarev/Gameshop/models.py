from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Game(models.Model):
    game_id = models.AutoField(primary_key=True, unique=True)
    game_name = models.CharField(max_length=70)
    production_date = models.DateField()
    firm = models.CharField(max_length=70)
    url_screen = models.URLField()
    genres = models.ManyToManyField('Genre', verbose_name="Жанры", related_name="games")
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=9,default=0)

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def __str__(self):
        return self.game_name


class CartGame(models.Model):
    owner = models.ForeignKey('Customer', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, verbose_name="Игра", on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    final_price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Общая цена",default=0)

    class Meta:
        verbose_name = "Игра в корзине"
        verbose_name_plural = "Игры в корзине"

    def __str__(self):
        return "Игра: {} (для корзины)".format(self.game.game_name)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.game.price
        super().save(*args, **kwargs)


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True, unique=True)
    owner = models.ForeignKey('Customer', null=True, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    games = models.ManyToManyField(CartGame, related_name="carts", blank=True)
    final_price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Общая цена", default=0)
    total_games = models.IntegerField(default=0)
    in_order = models.BooleanField(default=False)
    for_anon_user = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return str(self.cart_id)


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True, unique=True)
    genre_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.genre_name


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    orders = models.ManyToManyField('Order',verbose_name='Заказы покупателя', related_name='related_customer')


class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обраюотке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен'),
    )

    customer = models.ForeignKey(Customer, verbose_name='Покупатель', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60, verbose_name='Имя')
    last_name = models.CharField(max_length=60, verbose_name='Фамилия')
    email = models.EmailField(max_length=100, default="1")
    status = models.CharField(max_length=100, verbose_name='Статус заказа', choices=STATUS_CHOICES, default=STATUS_NEW)
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"



