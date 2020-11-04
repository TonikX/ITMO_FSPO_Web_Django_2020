from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from project_first_app.forms import *
from project_first_app.models import *


def view_users(request, pk):
    user = Owner.objects.get(pk=pk)

    context = {
        'user': user,
    }

    return render(request, 'index.html', context)


def all_users(request):
    context = {
        'users': Owner.objects.all(),
    }
    return render(request, 'all_users.html', context)


class Car(ListView):
    model = Car


def createOwner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()

    form = OwnerForm()
    context = {
        'form': form
    }

    return render(request, 'add_user.html', context)


def createCar(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "car_form.html", {'form': form})

