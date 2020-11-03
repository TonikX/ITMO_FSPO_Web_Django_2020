from django.contrib import admin
from .models import Car, Owner, Ownership, DriverLicense

admin.site.register(Car)
admin.site.register(Owner)
admin.site.register(Ownership)
admin.site.register(DriverLicense)

