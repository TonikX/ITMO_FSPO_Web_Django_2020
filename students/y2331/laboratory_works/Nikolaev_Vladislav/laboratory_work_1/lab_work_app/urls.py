from django.urls import path
from lab_work_app.views import *
urlpatterns = [
    path("route/", RouteView.as_view()),
    path("bus/", BusView.as_view()),
    path("race/", RaceView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("drivers/", DriversView.as_view())
]