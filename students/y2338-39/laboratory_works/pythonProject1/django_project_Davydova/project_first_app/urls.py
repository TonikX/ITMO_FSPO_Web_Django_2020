from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='general'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create')
]