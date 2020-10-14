from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic.list import ListView
from django.views.generic.base import View


def FlowerView(request):
    flowers = Flower.objects.all()
    return render(request, 'flowerlist.html', context={'flowers': flowers})


def ContractView(request):
    contract = Contract.objects.all()
    return render(request, 'contractlist.html', context={'contractslist': contract})


def DeliverView(request):
    deliver = Deliver.objects.all()
    return render(request, 'deliverlist.html', context={'deliverslist': deliver})


def FuncContractView(request):
    return render(request, 'menucontract.html')


def CompositionView(request):
    composition = Composition.objects.all()
    return render(request, 'compositionlist.html', context={'compositionslist': composition})


def FuncCompositionView(request):
    return render(request, 'menucomposition.html')


def FuncDeliverView(request):
    return render(request, 'menudeliver.html')


def Create_Flower(request):
    form = FlowerForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "Create_Flower.html", {'form': form})


def Create_Deliver(request):
    form = DeliverForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "Create_Deliver.html", {'form': form})


def Create_Composition(request):
    form = CompositionForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "Create_Composition.html", {'form': form})


def FuncFlowerView(request):
    return render(request, 'menuFlower.html')


def edit_flower(request, flower_id):
    try:
        flower = Flower.objects.get(flower_id=flower_id)
        if request.method == "POST":
            flower.flower_id = request.POST.get("flower_id")
            flower.name = request.POST.get("name")
            flower.sort = request.POST.get("sort")
            flower.cost = request.POST.get("cost")
            flower.save()
            return HttpResponseRedirect("/flowers/list/")
        else:
            return render(request, "editflower.html", context={"flower": flower})
    except Flower.DoesNotExist:
        return HttpResponseNotFound("<h2>Flower not found</h2>")


def edit_deliver(request, id_deliver):
    try:
        deliver = Deliver.objects.get(id_deliver=id_deliver)
        if request.method == "POST":
            deliver.id_deliver = request.POST.get("id_deliver")
            deliver.date_of_acceptance = request.POST.get("date_of_acceptance")
            deliver.date_of_execution = request.POST.get("date_of_execution")
            deliver.save()
            return HttpResponseRedirect("/deliver/list/")
        else:
            return render(request, "editdeliver.html", context={"deliver": deliver})
    except Deliver.DoesNotExist:
        return HttpResponseNotFound("<h2>deliver not found</h2>")


def edit_composition(request, composition_id):
    try:
        composition = Composition.objects.get(composition_id=composition_id)
        if request.method == "POST":
            composition.composition_id = request.POST.get("composition_id")
            composition.title = request.POST.get("title")
            composition.flower_id = request.POST.get("flower_id")
            composition.contract_id = request.POST.get("contract_id")
            composition.save()

            return HttpResponseRedirect("/composition/list/")
        else:
            return render(request, "editcomposition.html", context={"composition": composition})
    except Composition.DoesNotExist:
        return HttpResponseNotFound("<h2>composition not found</h2>")


def delete_composition(request, composition_id):
    try:
        composition = Composition.objects.get(composition_id=composition_id)
        composition.delete()
        return HttpResponseRedirect("/composition/list/")
    except Composition.DoesNotExist:
        return HttpResponseNotFound("<h2>composition not found</h2>")


def delete_flower(request, flower_id):
    try:
        flower = Flower.objects.get(flower_id=flower_id)
        flower.delete()
        return HttpResponseRedirect("/")
    except Flower.DoesNotExist:
        return HttpResponseNotFound("<h2>Flower not found</h2>")


def delete_deliver(request, id_deliver):
    try:
        deliver = Deliver.objects.get(id_deliver=id_deliver)
        deliver.delete()
        return HttpResponseRedirect("/")
    except Deliver.DoesNotExist:
        return HttpResponseNotFound("<h2>Deliver not found</h2>")


def Create_Contract(request):
    form = ContractForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "Create_Composition.html", {'form': form})


def edit_contract(request, id_contract):
    try:
        contract = Contract.objects.get(id_contract=id_contract)
        if request.method == "POST":
            contract.id_contract = request.POST.get("id_deliver")
            contract.id_deliver = request.POST.get("id_deliver")
            contract.save()
            return HttpResponseRedirect("/contract/list/")
        else:
            return render(request, "editcontract.html", context={"contract": contract})
    except Composition.DoesNotExist:
        return HttpResponseNotFound("<h2>composition not found</h2>")


def delete_contract(request, id_contract):
    try:
        contract = Deliver.objects.get(id_contract=id_contract)
        contract.delete()
        return HttpResponseRedirect("/contract/list/")
    except Deliver.DoesNotExist:
        return HttpResponseNotFound("<h2>Contract not found</h2>")


def MenuView(request):
    return render(request, 'menu.html')

# Create your views here.
