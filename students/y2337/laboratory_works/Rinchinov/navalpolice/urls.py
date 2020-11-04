from django.urls import path
from .views import *

urlpatterns = [
    path('addboat/', add_boat, name="addboat-url"),
    path('addpatrol/', add_patrol, name="addpatrol-url"),
    path('addpatrolling/', add_patrolling, name="addpatrolling-url"),
    path('patrols/', patrol_list, name="patrols-url"),
    path('boats/', boats_list, name="boats-url"),
    path('', patrolling_list, name="patrolings-url")
]