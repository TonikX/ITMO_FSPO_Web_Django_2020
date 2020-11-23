# Create your views here.
from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import Http404
from .models import Repair, Car, Workshop, Master, Type

from django.views.generic.edit import CreateView


def start(request):
    return render(request, 'Main.html')

def Adresses(request):
    worksh=Workshop.objects.all()
    return render(request, 'Adr.html', {'Work': worksh})

def MasterList(request):
    workshops=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        workshops = Master.objects.filter(workshop_id=search)
    return render(request, 'MasterList.html', {'workshops': workshops})

def RepairSearch(request):
    rep=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        rep = Repair.objects.filter(car_id=search)
    return render(request, 'RepairSearch.html', {'repairs': rep})

def CarSearch(request):
    avto=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        avto = Car.objects.filter(number=search)
    return render(request, 'CarSearch.html', {'cars': avto})

def PriceList(request):
    pr = Type.objects.all()
    return render(request, 'Price.html', {'price': pr})