from django.contrib import admin

from . import models

# Register your models here.
admin.site.register([
    models.Person,
    models.Group,
    models.Grade,
    models.Lesson,
    models.Schedule,
    models.Subject,
    models.ClassRoom
])
