from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Owner, Car
from .forms import OwnerForm
from django.views.generic.edit import CreateView


def details(request, Owner_id):
    try:
        owner = Owner.objects.get(pk=Owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owners/owner.html', {'owner': owner})

def listOwners(request):
    owners = Owner.objects.all()
    return render(request, 'owners/list.html', {'owners': owners})

def ownerForm(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OwnerForm()
    return render(request, 'samoletov_app/owner_view.html', {'form': form})

class CarAdd(CreateView):
    model = Car
    fields = ['mark', 'model']
    template_name = "samoletov_app/car_add.html"
    context_object_name = "cars"

class CarsList(ListView):
    model = Car
