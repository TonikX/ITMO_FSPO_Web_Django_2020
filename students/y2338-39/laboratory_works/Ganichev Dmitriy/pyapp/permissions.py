from rest_framework import permissions
from .models import AppUser


class IsAllowedForAppUserDirect(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        auser = AppUser.objects.get(user=request.user)

        if auser.role != 'A':
            viewname = type(view).__name__
            viewrole = {
                'HunterView': 'H',
                'FurPointView': 'W',
                'FactoryView': 'F',
                'MeDataView': 'HFW'
            }[viewname] or 'A'
            if viewrole:
                if auser.role not in viewrole:
                    return False

        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.user == request.user
