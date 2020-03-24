from django.shortcuts import render
from django.http import Http404
from platonov_app.models import users


def detail(request, users_id):
    try:
        p = users.objects.get(pk=users_id)
    except users.DoesNotExist:
        raise Http404("Users does not exists")
    return render(request, 'owner.html', {'users': p})
