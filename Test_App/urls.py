from django.urls import path
from .views import CarList, CarAdd

from . import views

urlpatterns = [
    path('owner/<int:Owner_id>/', views.details),
    path('ownerlist', views.OwnerList),
    path('carlist', CarList.as_view()),
    path('owneradd', views.ownerForm),
    path('caradd', CarAdd.as_view()),
]