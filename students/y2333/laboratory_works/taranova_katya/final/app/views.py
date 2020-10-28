from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import *
from .forms import *


class MyRegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"
    template_name = "singup.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def logout(request):
    return render(request, "logout.html")


def seat_add(request):
    context = {}
    form = SeatForm(request.POST or None)
    context['data_c'] = Carriage.objects.all()
    context['data_s'] = Seat.objects.all()
    print(form.is_valid())
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "seat.html", context)


def carriage_add(request):
    context = {}
    form = CarriageForm(request.POST or None)
    context['data_c'] = Carriage.objects.all()
    context['data_t'] = Train.objects.all()
    if form.is_valid():
        form.save()
        temp = Carriage.objects.get(reg_number_train=form.cleaned_data['reg_number_train'],
                                    number = form.cleaned_data['number'],
                                    number_of_seats = form.cleaned_data['number_of_seats'])
        for i in range(1, form.cleaned_data['number_of_seats']):
            b = Seat(id_carriage=temp.id, number=i, status='Свободно')
            b.save()
    context['form'] = form
    return render(request, "carriage.html", context)


def train_add(request):
    context = {}
    form = TrainForm(request.POST or None)
    context['data_t'] = Train.objects.all()
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "train.html", context)


def ticket_add(request, number, reg_number):
    context = {}
    form = TicketForm(request.POST or None)
    context['data_t'] = Ticket.objects.all()
    context = {'train': Train.objects.get(reg_number=reg_number), 'carriage': Carriage.objects.get(pk=number),
               'data_s': Seat.objects.all()}
    if form.is_valid():
        temp = Seat.objects.get(number=form.cleaned_data['number_seats'], id_carriage=form.cleaned_data['number_carriage'])
        temp.status = "Занят"
        temp.save()
        form.save()
    context['form'] = form
    return render(request, "ticket.html", context)


def buy(request):
    context = {'data_t': Train.objects.all(), 'data_c': Carriage.objects.all()}
    return render(request, "table.html", context)
