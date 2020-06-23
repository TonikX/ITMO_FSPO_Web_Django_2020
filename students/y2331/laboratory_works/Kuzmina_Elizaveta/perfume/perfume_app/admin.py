from django.contrib import admin
from perfume_app.models import *


class Admin(admin.ModelAdmin):
    pass


admin.site.register(Broker)
admin.site.register(Firm)
admin.site.register(Deal)
admin.site.register(OrderDeal)
admin.site.register(Product)
admin.site.register(Fabricator)
