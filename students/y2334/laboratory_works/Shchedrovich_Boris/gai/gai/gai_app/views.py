from django.shortcuts import render, redirect
from django.http import Http404
from .models import Car, Offence, Inspector, Judgement, Driver
from .forms import DriverForm, CarForm, InspectorForm, OffenceForm, JudgementForm


def menu(request):
    if request.method=='GET':
        if request.GET.get('car'):
             return redirect('car_add')
        if request.GET.get('driver'):
            return redirect('driver_add')
        if request.GET.get('inspector'):
            return redirect('inspector_add')
        if request.GET.get('judgement'):
            return redirect('judgement_add')

    context = {}
    return render(request, "menu.html", context)


def CarFormView(request):
    form = CarForm(request.GET or None)
    if form.is_valid():
        form.save()
    if request.GET.get('submit'):
        return redirect("menu")
    context = {}

    context['form'] = form
    return render(request, "car_add.html", context)

def DriverFormView(request):
    form = DriverForm(request.GET or None)
    if request.GET.get('submit'):
        if form.is_valid():
            form.save()
        return redirect("menu")
    context ={}


    context['form'] = form
    return render(request, "driver_add.html", context)

def InspectorFormView(request):
    form = InspectorForm(request.GET or None)
    if form.is_valid():
        form.save()
    if request.GET.get('submit'):
        return redirect("menu")
    context ={}


    context['form'] = form
    return render(request, "inspector_add.html", context)

def OffenceFormView(request):
    form = OffenceForm(request.GET or None)
    if form.is_valid():
        form.save()
    if request.GET.get('submit'):
        return redirect("menu")
    context ={}


    context['form'] = form
    return render(request, "offence_add.html", context)

def JudgementFormView(request):
    form = JudgementForm(request.GET or None)
    if form.is_valid():
        form.save()
    if request.GET.get('submit'):
        return redirect("menu")
    context ={}


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
