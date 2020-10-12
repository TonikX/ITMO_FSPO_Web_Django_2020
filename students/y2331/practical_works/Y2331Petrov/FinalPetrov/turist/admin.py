from django.contrib import admin
from turist.models import Bus
from turist.models import Route
from turist.models import Crew
from turist.models import Trips
# Register your models here.

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Crew)
admin.site.register(Trips)
