from django.urls import path
from perfume_app.views import *

urlpatterns = [
    path('broker/', BrokerView.as_view()),
    path('firm/', FirmView.as_view()),
    path('deal/', DealCRUDView.as_view()),  # post и get запросы
    path('deal/<int:pk>', DealCRUDView.as_view()),  # put и delete запросы
    path('fabricator/', FabricatorView.as_view()),
    path('product/', ProductCRUDView.as_view()),  # post и get запросы
    path('product/<int:pk>', ProductCRUDView.as_view()),  # put и delete запросы
    path('order_deal/', OrderDealView.as_view()),
]