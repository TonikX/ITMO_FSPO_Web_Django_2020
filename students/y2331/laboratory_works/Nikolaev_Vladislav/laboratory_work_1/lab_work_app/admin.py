from django.contrib import admin
from lab_work_app.models import *


class RouteAdmin(admin.ModelAdmin):
    list_display = ("routeName", "startCity", "finishCity", "distance")


class BusAdmin(admin.ModelAdmin):
    list_display = ("busName", "mileage", "busType", "busNumber")


class RaceAdmin(admin.ModelAdmin):
    list_display = ("dateStart", "dateFinish", "amount", "price", "state", "raceRoute", "raceBus")


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "fullName", "location", "birth_date", "position", "contacts")


class DriversAdmin(admin.ModelAdmin):
    list_display = ("person", "experience", "category", "driverBus")


admin.site.register(Route, RouteAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Drivers, DriversAdmin)
