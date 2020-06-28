"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path
from projectApp.views import voyage_view, login_view, register_view, user_view, new_voyage_view, new_trawler_view, trawler_view, AssignView, assign_view, award_view, operation_view
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('voyage/', voyage_view),
    path('', login_view),
    path('register/', register_view),
    path('account/', user_view),
    path('voyage/new/', new_voyage_view),
    path('trawler/new/', new_trawler_view),
    path('trawler/', trawler_view),
    path('assign/', assign_view),
    path('award/new/', award_view),
    path('stock/new', operation_view)
]
