from django.urls import path
from project_first_app import views

urlpatterns = [
    path('owner/<int:id>/',views.Owners)
]