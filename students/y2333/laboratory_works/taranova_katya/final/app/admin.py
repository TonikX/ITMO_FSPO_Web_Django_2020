from django.contrib import admin
from .models import *
models = [Train, Seat, Carriage, Ticket]
admin.site.register(models)
# Register your models here.
