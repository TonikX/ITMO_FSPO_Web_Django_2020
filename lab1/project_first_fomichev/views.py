from django.shortcuts import render

# Create your views here.

from .models import Owner

def ownerDetails(request, owner_id):
    o = Owner.objects.get(pk=owner_id)
    return render(request, 'ownerDetails.html', {'owner': o})

#from .models import Owner
#from django.http import Http404

# def ownerDetails(request, owner_id):
#    try:
#        o = Owner.objects.get(pk='owner_id')
#    except Owner.DoesNotExist:
#        raise Http404("User does not exist")
#    return render(request, 'ownerDetails.html', {'owner': o})
