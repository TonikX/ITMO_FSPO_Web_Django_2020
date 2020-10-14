from django.shortcuts import render, get_object_or_404, redirect
from app.models import Heli, Pilot, Flight, Crew, Ticket
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from app.forms import TicketForm
from django.views.generic import CreateView


def mainpage(request):
    flights = Flight.object.all()
    return render(request, "app/mainpage.html", {"flights": flights})


class LogoutView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect("/")


class RegisterView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login"

    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterView, self).form_valid(form)


def heli_list(request):
    helis = Heli.object.all()
    return render(request, "app/heli_list.html", {"helis": helis})


def pilot_list(request):
    pilots = Pilot.object.all()
    return render(request, "app/pilot_list.html", {"pilots": pilots})


def profile(request):
    tickets = Ticket.objects.all().filter(user_id=request.user.id)
    return render(request, "app/profile.html", {"tickets": tickets})


def cancel(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    ticket.delete()
    return render(request, "app/cancel.html", {"ticket": ticket})


class PilotCreate(CreateView):
    model = Pilot
    fields =['pilot_id','surname', 'position', 'birthdate', 'crew']


def flight_buy(request, pk):
    flight = get_object_or_404(Flight, id=pk)

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.ticket_id = 0
            form.user_id = request.user.id
            form.category = form.category
            form.flight = flight
            form.save()
            return redirect("/")
    else:
        form = TicketForm()
    return render(request, "app/buy.html", {"flight": flight, "form": form})
