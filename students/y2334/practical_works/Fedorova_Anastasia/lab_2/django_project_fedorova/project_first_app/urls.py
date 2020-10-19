from django.urls import path
from . import views
from .views import list_view, VehList, VehCreate

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('owner/list', list_view),
    path('owner/form', views.owner_form),
    path('vehicle/list', VehList.as_view()),
    path('vehicle/form', VehCreate.as_view())
]
