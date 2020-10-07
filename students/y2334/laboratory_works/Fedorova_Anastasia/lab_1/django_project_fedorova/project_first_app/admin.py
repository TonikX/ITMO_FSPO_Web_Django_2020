from django.contrib import admin
from .models import Owner
from .models import Ownership
from .models import Vehicle
from .models import License

# Register your models here.
admin.site.register(Owner)
admin.site.register(Vehicle)
admin.site.register(Ownership)
admin.site.register(License)

# login admin
# pass 1488
