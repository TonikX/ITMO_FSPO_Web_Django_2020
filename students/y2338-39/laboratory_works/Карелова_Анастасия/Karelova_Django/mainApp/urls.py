from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('exit', views.exit, name='exit'),
    path('start', views.start, name='start'),
    path('start_meeting', views.start_meeting, name='start_meeting'),
    path('start_pay', views.start_pay, name='start_pay'),
    path('profile', views.profile, name='profile'),
    path('divorce', views.DivorceListView.as_view(), name='Divorce'),
    path('advice', views.AdviceListView.as_view(), name='Advice'),
    path('crash', views.CrashListView.as_view(), name='Crash'),
    path('registration', views.registration, name='registration'),
    path('authorisation', views.authorisation, name='authorisation'),
]