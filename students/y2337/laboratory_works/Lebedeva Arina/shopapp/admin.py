from django.contrib import admin
from .models import *


admin.site.register(Developer)
admin.site.register(Game)
admin.site.register(CD)
admin.site.register(Customer)
admin.site.register(Order)

# Register your models here.