from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

# Create your views here.
from .models import Owner, Car
from .forms import OwnerForm


def ownerDetails(request, owner_id):
    o = Owner.objects.get(pk=owner_id)
    return render(request, 'owner_details.html', {'owner': o})


def allOwners(request):
    o = Owner.objects.all()
    return render(request, 'OwnersList.html', {'owners': o})


class AutoView(ListView):
    model = Car
    template_name = 'CarsList.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.all()
    # def get(self, request):
    #     a = Auto.objects.all()
    #     return render(request, 'CarsList.html', {'autos': a})


def create_owner(request):
    context = {}
    form = OwnerForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'owner_form.html', context)

class AutoCreate(CreateView):
    model = Car
    fields = ["make", "model", "color", "number"]
    template_name = 'car_form.html'
    success_url = 'create'
