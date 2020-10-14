from django.shortcuts import render, redirect
from django.template import RequestContext

from see_police.models import *
from .forms import *


# Вывод данных о всех патрульных.
def output_patrolman(request):
    patrolman = Patrolman.objects.filter(position="Капитан")
    return render(request, "see_patrol/patrolmanlist.html", {"patrolman": patrolman})

def editPatrolman(request, pk):
    context_instance=RequestContext(request)
    patrolman = Patrolman.objects.get(pk=pk)
    if request.method == 'POST':
        form = PatrolmanForm(request.POST, instance=patrolman)
        if form.is_valid():
            form.save()
            return redirect(output_profile, pk=pk)
    else:
        form = PatrolmanForm(instance=patrolman)
    return render(request, "see_patrol/editPatrolman.html", {"form": form})

# Вывод данных о результатах патрулирования
def output_patrol_result(request):
    patrol_result = Patrol_result.objects.all()
    patrol_water_area = Patrol_water_area.objects.all()
    return render(request, "see_patrol/patrol_resultlist.html",
                  {"patrol_result": patrol_result, 'patrol_water_area': patrol_water_area})


def create_patrol(request):
    if request.method == 'POST':
        form = PatrolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(createWaterArea)
    else:
        form = PatrolForm()
    return render(request, "see_patrol/createPatrol.html", {"form": form})


def createWaterArea(request):
    if request.method == 'POST':
        form = WaterAreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(create_patrol)
    else:
        form = WaterAreaForm()
    return render(request, "see_patrol/createWaterArea.html", {"form": form})


def output_profile(request, pk):
    patrolman = Patrolman.objects.get(pk=pk)
    return render(request, "see_patrol/profile.html", {"patrolman": patrolman})

# Профиль патрульного (информация, партулирования)
# Редактирование профиля
# Количество пойманных нарушителей
# Внести информацию о патрулировании
# Вывод капитанов
