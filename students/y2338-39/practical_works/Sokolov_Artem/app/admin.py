from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Animal)
admin.site.register(Diet)
admin.site.register(Feed)
admin.site.register(PeriodHistory)
admin.site.register(SalesHistory)
admin.site.register(Ticket)
admin.site.register(User)