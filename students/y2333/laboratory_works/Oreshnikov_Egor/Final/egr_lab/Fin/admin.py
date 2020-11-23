from django.contrib import admin

# Register your models here.
from .models import Master
from .models import Repair
from .models import Car
from .models import Workshop
from .models import Type



class Admin(admin.ModelAdmin):
    pass


admin.site.register(Master, Admin)
admin.site.register(Repair, Admin)
admin.site.register(Car, Admin)
admin.site.register(Workshop, Admin)
admin.site.register(Type, Admin)
