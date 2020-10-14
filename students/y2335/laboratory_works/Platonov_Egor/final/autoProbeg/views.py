from django.shortcuts import render, get_object_or_404, redirect
from autoProbeg.forms import *
from django.http import Http404


def auto_list(request):
    """Список продающихся авто"""
    autos = Auto.objects.filter(moderation=True)
    return render(request, 'probeg/auto_list.html', {"autos": autos})


def auto_single(request, pk):
    """Конкретное продающееся авто"""
    auto = get_object_or_404(Auto, id=pk)
    return render(request, 'probeg/auto_single.html', {'auto': auto})


def createAuto(request):
    """Добавить авто"""
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect(auto_list)
    else:
        form = AutoForm()
    return render(request,
                  "probeg/createAuto.html",
                  {'form': form})


def manageTool(request):
    if request.method == 'POST':
        if 'mark' in request.POST:
            return redirect(createMark)
        elif 'model' in request.POST:
            return redirect(createModel)
        elif 'transmission' in request.POST:
            return redirect(createTransmission)
        elif 'gear' in request.POST:
            return redirect(createGear)
        elif 'manage_autos' in request.POST:
            return redirect(manageAutoAnoun)
    if not request.user.groups.filter(name="manager").exists():
        raise Http404
    return render(request,
                  'probeg/manager.html')


def createMark(request):
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(manageTool)
    else:
        form = MarkForm()
    if not request.user.groups.filter(name="manager").exists():
        raise Http404
    return render(request,
                  "probeg/manage_mark.html",
                  {'form': form})


def createModel(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(manageTool)
    else:
        form = ModelForm()
    if not request.user.groups.filter(name="manager").exists():
        raise Http404
    return render(request,
                  "probeg/manage_model.html",
                  {'form': form})


def createTransmission(request):
    if request.method == 'POST':
        form = TransmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(manageTool)
    else:
        form = TransmissionForm()
    if not request.user.groups.filter(name="manager").exists():
        raise Http404
    return render(request,
                  "probeg/manage_transmission.html",
                  {'form': form})


def createGear(request):
    if request.method == 'POST':
        form = GearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(manageTool)
    else:
        form = GearForm()
    if not request.user.groups.filter(name="manager").exists():
        raise Http404
    return render(request,
                  "probeg/manage_gear.html",
                  {'form': form})


def manageAutoAnoun(request):
    autos = Auto.objects.filter(moderation=False)
    if request.method == 'POST':
        if 'accept' in request.POST:
            auto = Auto.objects.get(pk=int(request.POST['accept']))
            auto.moderation = True
            auto.save()
        elif 'deni' in request.POST:
            auto = Auto.objects.get(pk=int(request.POST['deni']))
            auto.delete()
        return redirect(manageAutoAnoun)
    if not request.user.groups.filter(name="manager").exists():
        raise Http404
    return render(request,
                  'probeg/manage_announcement.html',
                  {'autos': autos})