from django.urls import path
from . import views

urlpattern = [
    path('', views.get_judgements, name="judgement_list")
]