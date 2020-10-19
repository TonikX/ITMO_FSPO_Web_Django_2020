from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.catalog, name="catalog"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('accounts/profile/', views.toHomepage),
    path('cart/', views.cart, name='cart'),
    path('orders/', views.orders, name='orders'),
    path('admission/', views.admission, name='admission'),
    path('admissions/', views.getAdmissions, name='admissions')
]
