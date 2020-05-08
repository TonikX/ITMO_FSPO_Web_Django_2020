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
    return render(request, 'Test_App/owner/owner.html', {'owner': owner})

def OwnerList (request):
    owners = Owner.objects.all()
    return render(request, 'Test_App/owner/OwnerList.html', {'owners': owners})

def ownerForm(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OwnerForm()
    return render(request, 'Test_App/owner_view.html', {'form': form})

class CarAdd(CreateView):
    model = Car
    fields = ['Mark', 'Model']
    template_name = "Test_App/car_add.html"
    context_object_name = "cars"
    success_url = '/carlist'

class CarList(ListView):
    model = Car
    