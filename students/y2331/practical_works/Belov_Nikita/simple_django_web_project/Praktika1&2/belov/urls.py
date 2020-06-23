from django.urls import path, include
from belov import views
from .views import CarList, UserForm

urlpatterns = [
    path('<int:car_id>', views.detail),
    path('users', views.list_view),
    path('cars', CarList.as_view()),
    path('carform', views.create_car_view),
    path('userform', UserForm.as_view())
]

