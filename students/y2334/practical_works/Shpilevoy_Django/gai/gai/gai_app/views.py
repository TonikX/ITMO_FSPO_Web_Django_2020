from django.shortcuts import render
from django.http import Http404
from .models import Car, Offence, Inspector, Judgement, Driver

def get_judgements(request):
    try:
        judgements = Judgement.objects.all()
    except Judgement.DoesNotExist:
        raise Http404("No judgements")
    return render(request, "judgement_list.html", {"judgements": judgements})

