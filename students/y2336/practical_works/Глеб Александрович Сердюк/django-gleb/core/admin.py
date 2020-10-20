from django.contrib import admin

from . import models

# Register your models here.
admin.site.register([
    models.Jewelry,
    models.ProductInShoppingBag,
    models.Brand,
    models.ClientUser,
    models.ProductInPurchase,
    models.Purchase,
    models.Sale,
])
