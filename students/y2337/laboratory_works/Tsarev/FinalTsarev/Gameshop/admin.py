from django.contrib import admin


from .models import *

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Cart)
admin.site.register(CartGame)
admin.site.register(Customer)
admin.site.register(Order)


# Register your models here.
