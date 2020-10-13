from django.shortcuts import render, get_object_or_404, redirect
from app.models import Motorship, Tour, Ticket, Sailor
from app.forms import TicketForm, FindForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout


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


def motorship_list(request):
    motorships = Motorship.objects.all()
    return render(request, "app/motorship_list.html", {"motorships": motorships})


# def login(request):
#     return  render(login, "registration/login.html")

def find(request):
    if request.method == "POST":
        form = FindForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return redirect("/tour/" + str(form.motorship.id))
    else:
        form = FindForm()
    return render(request, "app/find.html", {"form": form})


def sailor_list(request):
    sailors = Sailor.objects.all()
    return render(request, "app/sailor_list.html", {"sailors": sailors})


def thanks(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    return render(request, "app/thanks.html", {"ticket": ticket})


def tickets(request):
    tickets = Ticket.objects.all().filter(user_id=request.user.id)
    return render(request, "app/tickets.html", {"tickets": tickets})


def tour_list(request):
    tours = Tour.objects.all()
    return render(request, "app/tours.html", {"tours": tours})


def tour(request, pk):
    tours = Tour.objects.all().filter(motorship_id=pk)
    return render(request, "app/tour.html", {"tours": tours})


def remove(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    ticket.delete()
    return render(request, "app/remove.html", {"ticket": ticket})


def tour_buy(request, pk):
    tour = get_object_or_404(Tour, id=pk)

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.ticket_id = 0
            form.user_id = request.user.id
            form.category = form.category
            form.tour = tour
            form.save()
            return redirect("/thanks/" + str(form.id))
    else:
        form = TicketForm()
    return render(request, "app/buy.html", {"tour": tour, "form": form})
