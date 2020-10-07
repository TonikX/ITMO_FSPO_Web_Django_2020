from django.contrib import admin
from app.models import Owner
from app.models import Car
from app.models import DriverLicense
from app.models import Ownership
from app.models import User


class Admin(admin.ModelAdmin):
    pass


admin.site.register(Owner, Admin)
admin.site.register(Car, Admin)
admin.site.register(DriverLicense, Admin)
admin.site.register(Ownership, Admin)
admin.site.register(User, Admin)