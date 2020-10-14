from django.urls import path
from .views import CarsList, CarAdd

from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.details),
    path('owners/', views.listOwners),
    path('cars/', CarsList.as_view()),
    path('owneradd', views.ownerForm),
    path('caradd', CarAdd.as_view()),
]