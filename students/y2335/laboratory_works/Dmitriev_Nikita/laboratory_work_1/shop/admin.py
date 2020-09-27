from django.contrib import admin
from .models import *

admin.site.register(Cassette)
admin.site.register(Seller)
admin.site.register(Admission)
admin.site.register(Order)
admin.site.register(CassetteInOrder)
