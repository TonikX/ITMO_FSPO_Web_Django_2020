from django.contrib import admin
from .models import CarOwner, DriverDocument, Car, Ownership

# Register your models here.

admin.site.register(CarOwner)
admin.site.register(DriverDocument)
admin.site.register(Car)
admin.site.register(Ownership)