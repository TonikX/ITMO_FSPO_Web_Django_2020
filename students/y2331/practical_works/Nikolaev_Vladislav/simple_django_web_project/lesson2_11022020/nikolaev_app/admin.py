from django.contrib import admin
from .models import User, Auto, AutoUser, DriverLicence
admin.site.register(User)
admin.site.register(Auto)
admin.site.register(AutoUser)
admin.site.register(DriverLicence)
# Register your models here.
