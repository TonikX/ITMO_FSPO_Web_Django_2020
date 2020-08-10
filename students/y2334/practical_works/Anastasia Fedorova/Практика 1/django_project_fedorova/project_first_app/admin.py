from django.contrib import admin
from .models import Deus
from .models import Machina
from .models import ExMachina
from .models import License


# Register your models here.

admin.site.register(Deus)
admin.site.register(Machina)
admin.site.register(ExMachina)
admin.site.register(License)

# login admin
# password password
