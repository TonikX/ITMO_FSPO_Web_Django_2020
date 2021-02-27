from django.urls import path
from . import views

urlpatterns = [
    path('', views.auto_list, name="auto_list"),
    path('auto/<int:pk>', views.auto_single, name="auto_single"),
    path('sellauto/', views.createAuto, name="createAuto"),
    path('manager/', views.manageTool, name="manageTool"),
    path('manager/mark', views.createMark, name="createMark"),
    path('manager/model', views.createModel, name="createModel"),
    path('manager/transmission', views.createTransmission, name="createTransmission"),
    path('manager/gear', views.createGear, name="createGear"),
    path('manager/announcement', views.manageAutoAnoun, name="manageAutoAnoun"),
]