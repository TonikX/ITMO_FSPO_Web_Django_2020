from django.contrib import admin


# Register your models here.
# password zoinks
from perfum.models import Broker, Buyer, Deal, Product, Seller, Supply

admin.register(Broker)
admin.register(Buyer)
admin.register(Deal)
admin.register(Product)
admin.register(Seller)
admin.register(Supply)
