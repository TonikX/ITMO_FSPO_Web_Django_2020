from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Owner



def Owners(request, id):
    try:
        owner = Owner.objects.get(id = id)
        return render(request,"owner.html",{"owner": owner})
    except Owner.DoesNotExist:
        return HttpResponseNotFound("<h2>Owner not found</h2>")