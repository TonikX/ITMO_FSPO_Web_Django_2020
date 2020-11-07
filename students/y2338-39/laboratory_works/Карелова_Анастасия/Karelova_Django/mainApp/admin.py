from django.contrib import admin
from .models import Lawyer, Client, Payment, Deal, CurrentClient, Meeting
admin.site.register(Lawyer)
admin.site.register(Client)
admin.site.register(Payment)
admin.site.register(Deal)
admin.site.register(CurrentClient)
admin.site.register(Meeting)
# Register your models here.
