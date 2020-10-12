from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.dispatch import receiver
from allauth.account.signals import user_logged_in
# Create your views here.
username = {}


@receiver(user_logged_in)
def user_logged_in_(request, user, **kwargs):
    global username
    username = user


def show_trips(request):
    tr = Trips.objects.all()
    return render(request, 'turist/main.html', context={'trips': tr})


def details(request, slug):
    nam = Trips.objects.get(slug__exact=slug)
    return render(request, 'turist/inf.html', context={'n': nam, 'us': str(username)})


def zakazik(request, slug):
    ob = Trips.objects.get(slug__exact=slug)
    ob.Qty = ob.Qty + 1
    ob.turi = str(username)
    ob.save()
    return render(request, 'turist/zakazio.html', context={'o': ob})
