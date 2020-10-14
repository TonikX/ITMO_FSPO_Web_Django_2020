from django.shortcuts import render


from django.http import Http404
from django.shortcuts import render
from project_first_app.models import CarOwner

def detail(request, CarOwner_id):

    try:
        p = CarOwner.objects.get(pk=CarOwner_id)

    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")

    return render(request, 'project_first_app/CarOwner.html', {'CarOwner': p})