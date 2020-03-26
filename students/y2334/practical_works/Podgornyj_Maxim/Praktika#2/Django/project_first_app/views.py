from django.shortcuts import render
from project_first_app.models import Person
from project_first_app.models import Car
from django.views.generic.list import ListView


# Create your views here.


class CarView(ListView):
    model = Car


def list_view(request):
    context = {"dataset": Person.objects.all()}

    return render(request, "list_view.html", context)

