from django.contrib import admin
from .models import DriverLicense
from .models import CarOwner
from .models import Owning
from .models import Car

admin.site.register(CarOwner)
admin.site.register(DriverLicense)
admin.site.register(Owning)
admin.site.register(Car)