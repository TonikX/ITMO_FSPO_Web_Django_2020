from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Owner, Car


def details(request, Owner_id):
    try:
        owner = Owner.objects.get(pk=Owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'Test_App/owner/owner.html', {'owner': owner})

def OwnerList (request):
    owners = Owner.objects.all()
    return render(request, 'Test_App/owner/OwnerList.html', {'owners': owners})

class CarList(ListView):
    model = Car