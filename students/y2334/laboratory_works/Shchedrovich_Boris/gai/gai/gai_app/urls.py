from django.urls import path, re_path
from . import views

urlpatterns = [
    path('judgement/', views.get_judgements, name="judgement_list"),
    path('driver/<int:driver_id>/', views.get_driver_info),
    path('offence/', views.get_deprivation_offences, name="offence"),
    path('', views.menu, name='menu'),
    path('driver_add/', views.DriverFormView, name="driver_add"),
    path('car_add/', views.CarFormView, name="car_add"),
    path('inspector_add/', views.InspectorFormView, name="inspector_add"),
    path('judgement_add/', views.JudgementFormView, name="judgement_add"),
    path('offence_add/', views.OffenceFormView, name="offence_add"),
]