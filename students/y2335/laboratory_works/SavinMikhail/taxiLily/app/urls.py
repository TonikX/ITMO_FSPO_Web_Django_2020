from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', MyRegisterFormView.as_view(), name="signup"),
    path('', freeCar, name="freeCar"),
    path('tariff', tariff, name="tariff"),
    path('account/<int:accountId>', account, name="account"),
    path('order_creat/<int:taxis_id>', orderCreate, name="orderCreate"),
    path('order/<int:order_id>', order, name="order"),
    path('orderFinish/<int:order_id>', orderFinish, name="orderFinish"),
    ]