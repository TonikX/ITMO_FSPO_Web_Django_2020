from django.urls import path

from . import views

urlpatterns = [
    path('Owner/<int:Owner_id>/', views.details),
]
