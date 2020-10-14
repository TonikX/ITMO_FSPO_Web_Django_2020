from django.contrib import admin
from app.models import Heli, Pilot, Flight, Crew, Ticket

admin.site.register(Heli)
admin.site.register(Pilot)
admin.site.register(Flight)
admin.site.register(Crew)
admin.site.register(Ticket)

