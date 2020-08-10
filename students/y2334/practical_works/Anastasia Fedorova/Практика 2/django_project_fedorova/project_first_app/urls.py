from django.urls import path
from . import views
from .views import list_view

urlpatterns = [
    path('<int:deus_id>/', views.detail),
    path('list/', list_view),
    path('owform', views.deus_form)
]
