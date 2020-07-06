from django.urls import path
from .views import *

urlpatterns = [
    path('', show_trips),
    path('turist/<str:slug>/', details, name='route_detail'),
    path('turist/zakazik/<str:slug>/', zakazik, name='zakaz')
]
