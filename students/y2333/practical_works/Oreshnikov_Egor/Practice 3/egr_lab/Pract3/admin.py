from django.contrib import admin

# Register your models here.
from .models import People
from .models import User
from .models import Car
from .models import License
from .models import Ownership


class Admin(admin.ModelAdmin):
    pass


admin.site.register(People, Admin)
admin.site.register(User, Admin)
admin.site.register(Car, Admin)
admin.site.register(License, Admin)
admin.site.register(Ownership, Admin)