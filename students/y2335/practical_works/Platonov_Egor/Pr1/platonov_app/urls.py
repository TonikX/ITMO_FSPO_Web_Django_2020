from . import views

from django.urls import path

urlpatterns = [
    path('articles/<int:users_id>/', views.detail)
]
