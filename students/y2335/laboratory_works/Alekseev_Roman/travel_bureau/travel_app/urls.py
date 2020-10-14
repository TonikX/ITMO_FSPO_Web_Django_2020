from django.conf.urls import url
from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
url(r"^crewform/",login_required(CrewMemberCreateView.as_view()), name="crew_form"),
path('crewlist/', views.CrewList, name = 'crew_list'),
url(r"^home/", HomePageView.as_view() ,name="home"),
url(r"^excursionform/",login_required(ExcursionCreateView.as_view()), name="excursion_form"),
url(r"^excursions/",ExcursionList.as_view(), name="excursion_list"),
path('excursion/<int:excursion_id>', views.excursionDetail, name = 'excursion'),
url(r"^buses/",BusList.as_view(), name="bus_list"),
url(r"^routes/",RouteList.as_view(), name="route_list"),
url(r"^routeform/",login_required(RouteCreateView.as_view()), name="triproute_form"),
url(r"^busform/",login_required(BusCreateView.as_view()), name="bus_form"),
path('accounts/', include('django.contrib.auth.urls', ),name='login'),
path('register/', views.RegisterView.as_view(), name = 'register'),
path('logout/', views.LogoutView.as_view(), name = 'logout'),
]