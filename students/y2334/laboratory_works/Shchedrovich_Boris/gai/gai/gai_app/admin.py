from django.contrib import admin
from .models import Car, Offence, Driver, Inspector, Judgement

admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Inspector)
admin.site.register(Offence)
admin.site.register(Judgement)