from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(AppUser)
admin.site.register(Hunter)
admin.site.register(FurPoint)
admin.site.register(FurFactory)
admin.site.register(FurDelivery)
admin.site.register(FurShipment)
