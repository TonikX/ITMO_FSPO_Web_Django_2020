from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index),
    path('catalog/', views.JewelryListView.as_view(), name='jewelry-list'),
    path('sale/', views.SaleListView.as_view(), name='sale-list'),
    path('brand/', views.BrandListView.as_view(), name='brand-list'),
    path('brand/<int:pk>/', views.BrandDetailView.as_view(), name='brand-detail'),
    path('jewelry/<int:pk>/', views.JewelryDetailView.as_view(), name='jewelry-detail'),

    path('add/<int:item_id>/', views.add_item_to_shopping_bag, name='add-item'),
    path('delete/<int:pk>/', views.delete_item_from_shopping_bag, name='delete-item'),
    path('shopping/', views.ShoppingBagListView.as_view(), name='shopping'),
    path('create_purchase', views.create_purchase, name='create-purchase'),
    path('purchase/<int:pk>/', views.PurchaseDetailView.as_view(), name='purchase-detail'),

    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
