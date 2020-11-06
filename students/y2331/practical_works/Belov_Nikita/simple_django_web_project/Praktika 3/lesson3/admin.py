from django.contrib import admin

# Register your models here.

from .models import Owner
from .models import Car
from .models import License
from .models import Ownership
from .models import Usr

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(License)
admin.site.register(Ownership)
admin.site.register(Usr)