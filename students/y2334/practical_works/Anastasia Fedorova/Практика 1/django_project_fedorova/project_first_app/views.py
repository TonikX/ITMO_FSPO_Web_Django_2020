from django.shortcuts import render
from project_first_app.models import Deus, License
from django.http import Http404


# Create your views here.
def detail(request, deus_id):
    try:
        p = Deus.objects.get(pk=deus_id)
        l = License.objects.get(pk=deus_id)
    except Deus.DoesNotExist:
        raise Http404('This person does not exist.')
    req_data = {
        'objd': p,
        'objl': l
    }
    return render(request, 'deus.html', req_data)
