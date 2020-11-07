from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    path('', views.game_list, name="game_list"),
    path('single/<int:pk>', views.game_single, name="game_single"),
    path("game/add_book/", views.AddGame.as_view(), name="add_game"),
    path("game/update/<int:pk>", views.UpdateGame.as_view(), name="game/update/"),
    path("game/delete/<int:pk>", views.DeleteGame.as_view(), name="game_delete"),

    path("developer/add_author/", views.AddDeveloper.as_view(), name="add_developer"),
    path("developer/update/<int:pk>", views.UpdateDeveloper.as_view(), name="developer/update/"),
    path('developer/list/', views.ListDeveloper.as_view(), name="developer_list"),
    path("developer/delete/<int:pk>", views.DeleteDeveloper.as_view(), name="developer_delete"),

    path("cd/add/", views.AddCD.as_view(), name="add_cd"),
    path("cd/update/<int:pk>", views.UpdateCD.as_view(), name="cd/update/"),
    path('cd/list/', views.ListCD.as_view(), name="cd_list"),
    path("cd/delete/<int:pk>", views.DeleteCD.as_view(), name="cd_delete"),

    path("customer/add/", views.AddCustomer.as_view(), name="add_customer"),
    path("customer/update/<int:pk>", views.UpdateCustomer.as_view(), name="customer/update/"),
    path('customer/list/', views.ListCustomer.as_view(), name="customer_list"),
    path("customer/delete/<int:pk>", views.DeleteCustomer.as_view(), name="customer_delete"),

    path("order/add/", views.AddOrder.as_view(), name="add_order"),
    path("order/update/<int:pk>", views.UpdateOrder.as_view(), name="order/update/"),
    path('order/list/', views.ListOrder.as_view(), name="order_list"),
    path("order/delete/<int:pk>", views.DeleteOrder.as_view(), name="order_delete"),

]