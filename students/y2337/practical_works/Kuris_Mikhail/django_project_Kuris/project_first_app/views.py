from django.http import Http404
from django.shortcuts import render, get_object_or_404
from project_first_app.models import *


def view_users(request, pk):
    user = get_object_or_404(Owner, pk=pk) #Person.objects.get(2)

    context = {
        'user': user,
    }

    return render(request, 'index.html', context)
