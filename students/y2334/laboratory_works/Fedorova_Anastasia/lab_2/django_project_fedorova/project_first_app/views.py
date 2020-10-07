from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, CreateView

from project_first_app.forms import OwnerForm
from project_first_app.models import Owner, Vehicle


# Create your views here.


def detail(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404('This person does not exist')
    req_data = {
        'obj_id': p
    }
    return render(request, 'Owner_detail.html', req_data)


def list_view(request):
    context = {"dataset": Owner.objects.all()}
    return render(request, "list_view.html", context)


class VehList(ListView):
    model = Vehicle


class VehCreate(CreateView):
    model = Vehicle
    fields = '__all__'


def owner_form(request):
    context = {}
    form = OwnerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner_form.html", context)
