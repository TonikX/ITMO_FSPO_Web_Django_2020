from django.contrib import admin

from .models import (Owner)
from .models import (Have)
from .models import (Car)
from .models import (Owner_Addition)

admin.site.register(Owner)
admin.site.register(Have)
admin.site.register(Car)
admin.site.register(Owner_Addition)
# Register your models here.