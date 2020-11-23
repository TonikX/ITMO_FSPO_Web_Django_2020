from django.shortcuts import render


# Create your views here.
from django.http import Http404
from .models import User
from .models import License



def detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        License_id=user_id
        lic = License.objects.get(pk=License_id)
        except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'owner.html', {'User': user, 'License': lic})
