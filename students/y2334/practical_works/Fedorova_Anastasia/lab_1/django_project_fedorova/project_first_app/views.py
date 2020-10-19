from django.shortcuts import render
from django.http import Http404
from project_first_app.models import Owner


# Create your views here.


def detail(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404('This person does not exist')
    req_data = {
        'obj_id': p
    }
    return render(request, 'Owner_detail.html', req_data)
