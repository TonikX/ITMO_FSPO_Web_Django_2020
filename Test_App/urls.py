from django.urls import path
from . import views
from .views import CarList

urlpatterns = [
    path('owner/<int:Owner_id>/', views.details),
    path('ownerlist', views.OwnerList),
    path('carlist', CarList.as_view())
]