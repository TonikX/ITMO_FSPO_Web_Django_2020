from django.urls import path, include
from project_first_app.views import *

urlpatterns = [
    path('user/<int:pk>', view_users, name='view_users'),
    path('users', all_users),
    path('cars', Car.as_view(), name='cars'),
    path('adduser', createOwner),
    path('addcar', createCar)
]