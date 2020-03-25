from django.contrib import admin
from django.urls import path, include
from nikolaev_app import views

urlpatterns = [
    path('<int:question_id>/', views.detail)
]