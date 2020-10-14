from django.urls import path, include
from . import views
from .views import PilotCreate

urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('heli_list/', views.heli_list, name="heli_list"),
    path('pilot_list/', views.pilot_list, name="pilot_list"),
    path("profile/", views.profile, name="profile"),
    path("buy/<int:pk>", views.flight_buy, name="flight_buy"),
    path('cancel/<int:pk>', views.cancel, name="cancel"),
    path('pilot_form/', PilotCreate.as_view(success_url='pilot_form')),

]