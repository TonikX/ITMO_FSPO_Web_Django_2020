from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:deus_id>/', views.detail)
]
