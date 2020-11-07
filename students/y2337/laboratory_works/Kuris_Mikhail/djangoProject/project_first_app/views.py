from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from project_first_app.forms import *
from project_first_app.models import *
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound


def index(request):
    orgs = Organizations.objects.all()
    return render(request, 'index.html', {'title': 'Фирмы', 'orgs': orgs})


def get_items(request):
    items = Items.objects.all()
    return render(request, 'items.html', {'title': 'Изделия', 'items': items})

def get_fairs(request):
    fairs = Fair.objects.all()
    return render(request, 'fairs.html', {'title': 'Ярмарки', 'fairs': fairs})


def get_results(request):
    results = Results.objects.all()
    return render(request, 'results.html', {'title': 'Результаты', 'results': results})


def deleteItem(request, id):
    try:
        item = Items.objects.get(id=id)
        item.delete()
        return HttpResponseRedirect("/items")
    except Items.DoesNotExist:
        return HttpResponseNotFound("<h2>Items not found</h2>")


class AddItem(CreateView):
    model = Items
    form_class = AddItemForm
    template_name = "add.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect("/items")

class UpdateItem(UpdateView):
    model = Items
    form_class = AddItemForm
    template_name = "add.html"

    def get_success_url(self):
        return reverse('items')


def deleteResult(request, item_id):
    try:
        item = Results.objects.get(item_id=item_id)
        item.delete()
        return HttpResponseRedirect("/results")
    except Items.DoesNotExist:
        return HttpResponseNotFound("<h2>Result not found</h2>")


class AddRes(CreateView):
    model = Results
    form_class = AddResForm
    template_name = "add.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect("/results")


class UpdateRes(UpdateView):
    model = Results
    form_class = AddResForm
    template_name = "add.html"

    def get_success_url(self):
        return reverse('results')