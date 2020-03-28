from django.http import Http404
from django.shortcuts import render
from .models import Owner


def details(request, Owner_id):
    try:
        owner = Owner.objects.get(pk=Owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner/owner.html', {'owner': owner})