from django.shortcuts import render
from .models import Patrolling, Patrol, Boat
from .forms import *
from django.http import HttpResponseRedirect


# Create your views here.
def patrol_list(req):
    patrols = Patrol.objects.all()
    return render(req, "patrol_list.html", context={"patrol_list": patrols})

def boats_list(req):
    boats = Boat.objects.all()
    return render(req, "boat_list.html", context={"boat_list": boats})

def patrolling_list(req):
    patrollings = Patrolling.objects.all()
    return render(req, "patrolling_list.html", context={"patrolling_list": patrollings})


def add_boat(req):
    form = BoatForm(req.POST or None)
    if form.is_valid():
        boat_new = form.save()
        boat_new.id = form.cleaned_data['id']
        boat_new.name = form.cleaned_data['name']
        boat_new.save()
        return HttpResponseRedirect('/')
    return render(req, "add.html", {'form': form})


def add_patrol(req):
    form = PatrolForm(req.POST or None)
    if form.is_valid():
        patrol_new = form.save()
        patrol_new.boat_id = form.cleaned_data['boat_id']
        patrol_new.id = form.cleaned_data['id']
        patrol_new.name = form.cleaned_data['name']
        patrol_new.age = form.cleaned_data['age']
        patrol_new.exp = form.cleaned_data['exp']
        patrol_new.position = form.cleaned_data['position']
        patrol_new.save()
        return HttpResponseRedirect('/')
    return render(req, "add.html", {'form': form})


def add_patrolling(req):
    form = PatrollingForm(req.POST or None)
    if form.is_valid():
        patrolling_new = form.save()
        patrolling_new.boat_id = form.cleaned_data['boat_id']
        patrolling_new.area_id = form.cleaned_data['area_id']
        patrolling_new.date = form.cleaned_data['date']
        patrolling_new.count = form.cleaned_data['count']
        patrolling_new.save()
        return HttpResponseRedirect('/')
    return render(req, "add.html", {'form': form})

