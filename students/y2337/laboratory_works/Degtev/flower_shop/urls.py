from .views import *
from django.urls import path, include
from . import views

urlpatterns = [
    path('flowers/list/', FlowerView),
    path('flowers/create/', Create_Flower),
    path('flowers/', FuncFlowerView, name='Flower'),
    path('', MenuView, name='Menu'),
    path('flowers/list/editflower/<int:flower_id>', views.edit_flower),
    path('flowers/list/del/<int:flower_id>', delete_flower),

    path('composition/list/', CompositionView),
    path('composition/create/', Create_Composition),
    path('composition/', FuncCompositionView, name='Composition'),
    path('composition/list/editcomposition/<int:composition_id>', views.edit_composition),
    path('composition/list/del/<int:composition_id>', views.delete_composition),

    path('deliver/list/', DeliverView),
    path('deliver/create/', Create_Deliver),
    path('deliver/', FuncDeliverView, name='Deliver'),
    path('deliver/list/editdeliver/<int:id_deliver>', views.edit_deliver),
    path('deliver/list/del/<int:id_deliver>', views.delete_deliver),

    path('contract/list/', ContractView),
    path('contract/create/', Create_Contract),
    path('contract/', FuncContractView, name='Contract'),
    path('contract/list/editcontract/<int:id_contract>', views.edit_contract),
    path('contract/list/del/<int:id_contract>', views.delete_contract),

]
