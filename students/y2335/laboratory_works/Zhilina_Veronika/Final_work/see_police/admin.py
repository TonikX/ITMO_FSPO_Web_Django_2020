from django.contrib import admin
from see_police.models import *

admin.site.register(Patrolman)
admin.site.register(Patrolman_has_patrol_result)
admin.site.register(Patrol_result)
admin.site.register(Patrol_water_area)


