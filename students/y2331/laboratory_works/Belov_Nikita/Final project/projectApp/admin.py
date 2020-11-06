from django.contrib import admin
from projectApp.models import ExtendedUserModel, Trawlers, Awards, FishOperation, Voyage, Crews

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'job_type']


class TrawlerAdmin(admin.ModelAdmin):
    list_display = ['name']


class VoyageAdmin(admin.ModelAdmin):
    list_display = ['tId', 'startDate', 'endDate']


class AwardAdmin(admin.ModelAdmin):
    list_display = ['uId', 'awardSize', 'date']


class FOpAdmin(admin.ModelAdmin):
    list_display = ['date', 'price']


class CrewAdmin(admin.ModelAdmin):
    list_display = ['tId', 'uId']


admin.site.register(ExtendedUserModel, UserAdmin)
admin.site.register(Trawlers, TrawlerAdmin)
admin.site.register(Voyage, VoyageAdmin)
admin.site.register(Awards, AwardAdmin)
admin.site.register(FishOperation, FOpAdmin)
admin.site.register(Crews, CrewAdmin)