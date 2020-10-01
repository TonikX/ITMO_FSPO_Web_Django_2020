from django.shortcuts import render
from django.http import Http404
from .models import Car, Offence, Inspector, Judgement, Driver
from .forms import DriverForm, CarForm, InspectorForm, OffenceForm, JudgementForm


def CarFormView(request):
    context = {}

    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "car_add.html", context)

def DriverFormView(request):
    context ={}

    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "driver_add.html", context)

def InspectorFormView(request):
    context ={}

    form = InspectorForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "inspector_add.html", context)

def OffenceFormView(request):
    context ={}

    form = OffenceForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "offence_add.html", context)

def JudgementFormView(request):
    context ={}

    form = JudgementForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "judgement_add.html", context)



def get_judgements(request):
    try:
        judgement = Judgement.objects.all()
    except Judgement.DoesNotExist:
        raise Http404("No judgements")
    return render(request, "judgement_list.html", {"judgements": judgement})

def get_driver_info(request, driver_id):
    try:
        driver = Driver.objects.get(pk=driver_id)
    except Driver.DoesNotExist:
        raise Http404("No drivers")
    return render(request, "driver_info.html", {"driver": driver})

def get_deprivation_offences(request):
    try:
        offences = Offence.objects.exclude(term_deprivation=0)
        offence = Judgement.objects.filter(offence__in=offences)
    except Offence.DoesNotExist:
        raise Http404("No offences")
    return render(request, "offence.html", {"offence": offence})
