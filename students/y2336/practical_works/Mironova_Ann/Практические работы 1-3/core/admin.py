from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(Possession)
admin.site.register(License)
