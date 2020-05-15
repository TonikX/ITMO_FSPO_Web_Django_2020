from django.contrib import admin

from .models import User
from .models import Car
from .models import Owner
from .models import Vladenie
from .models import License

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Owner)
admin.site.register(Vladenie)
admin.site.register(License)
