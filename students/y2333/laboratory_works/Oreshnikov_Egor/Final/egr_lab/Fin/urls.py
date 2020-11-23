
from django.urls import path
#from .views import CarList
from .views import start
from . import views
from . import forms

urlpatterns = [
        path('', views.start),
        path('workshops', views.Adresses),
        path('masters', views.MasterList),
        path('repairs', views.RepairSearch),
        path('cars', views.CarSearch),
        path('price', views.PriceList),
       

   ]

