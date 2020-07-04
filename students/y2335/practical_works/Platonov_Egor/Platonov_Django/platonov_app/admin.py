from django.contrib import admin

from .models import Auto
from .models import Owner
from .models import Owning
from .models import DriveLic

admin.site.register(Auto)
admin.site.register(Owner)
admin.site.register(Owning)
admin.site.register(DriveLic)
