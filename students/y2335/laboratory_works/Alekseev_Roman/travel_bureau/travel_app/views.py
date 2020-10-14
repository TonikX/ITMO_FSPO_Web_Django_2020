from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.http import Http404
from .models import *
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

class HomePageView(TemplateView):
    template_name = 'home.html'



def excursionDetail(request,excursion_id):
    exc = Completed_trip.objects.get(pk = excursion_id)
    members = Crew_member.objects.all().filter(bus_id = exc.bus_id.id)
    return render(request, 'Excursiondetail.html', {'excursion':exc,'members':members})

class ExcursionList(ListView):
    model = Completed_trip
    template_name = 'excursion_list.html'

class BusCreateView(CreateView):
    model = Bus
    fields = {'id','name','mileage'}
    template_name = 'bus_form.html'
    success_url = '/busform'
    def get_queryset(self):
        return Bus.objects.all()

class BusList(ListView):
    model = Bus
    template_name = 'bus_list.html'


class RouteCreateView(CreateView):
    model = Excursion_route
    fields = {'id','name','start_location','end_location','length'}
    template_name = 'triproute_form.html'
    success_url = '/routeform'


class RouteList(ListView):
    model = Excursion_route
    template_name = 'route_list.html'


class CrewMemberCreateView(CreateView):
    model = Crew_member
    fields = {'id', 'second_name', 'exp', 'category', 'adress', 'birth_date', 'bus_id' }
    template_name = 'crew_form.html'
    success_url = '/crewform'


def CrewList(request):
    d = Crew_member.objects.all().filter(category = 'Водитель')
    g = Crew_member.objects.all().filter(category='Гид')
    s = Crew_member.objects.all().filter(category='Стюардесса')
    return render(request, 'crew_list.html', {'drivers':d,'gids':g,'steward':s})


class ExcursionCreateView(CreateView):
    model = Completed_trip
    fields = {'id','end_date', 'start_date', 'price','n_passengers', 'bus_id', 'route_id'}
    template_name = 'excursion_form.html'
    success_url = '/excursionform'


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/home/")


class RegisterView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login"

    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)