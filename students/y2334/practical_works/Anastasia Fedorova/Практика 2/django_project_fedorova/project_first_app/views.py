from django.shortcuts import render
from django.views.generic import ListView
from .forms import DeusForm
from django.views.generic.edit import CreateView

from project_first_app.models import Deus, Machina
from django.http import Http404


# Create your views here.
def detail(request, deus_id):
    try:
        p = Deus.objects.get(pk=deus_id)
    except Deus.DoesNotExist:
        raise Http404('This person does not exist.')
    req_data = {
        'objd': p
    }
    return render(request, 'deus.html', req_data)


def list_view(request):
    context = {"dataset": Deus.objects.all()}
    return render(request, "list_view.html", context)


class Kars_list(ListView):
    model = Machina


def deus_form(request):
    context = {}
    form = DeusForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owform.html", context)


class KarsCreate(CreateView):
    model = Machina
    fields = '__all__'
