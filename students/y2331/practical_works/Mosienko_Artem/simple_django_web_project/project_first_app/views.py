from django.shortcuts import render
from django.views.generic.list import ListView
from project_first_app.models import Owner, Car
from project_first_app.forms import OwnerForm
from django.http import Http404
from django.views.generic.edit import CreateView

def owner(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("No such owner.")
    return render(request, 'owner.html', {'owner':o})


def get_owners(request):
    o = Owner.objects.all()
    return render(request, 'get_owners.html', {'owners':o})


class GetCarsList(ListView):
    template_name = 'get_cars.html'
    model = Car


def create_owner_form(request):
    context = {}

    form = OwnerForm(
        request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, "create_owner.html", context)


class CreateCarForm(CreateView):
    template_name = 'create_car.html'
    model = Car
    fields = [
        'make',
        'model',
        'color',
        'registration_plate'
        ]
