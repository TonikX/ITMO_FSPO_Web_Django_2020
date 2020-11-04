from django.urls import path, include
from django.urls import reverse
from .views import *


urlpatterns = [
    path('accounts/register/', MyRegisterFormView.as_view(), name="signup_url"),
    path('accounts/logout/', logout, name="logout_url"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('train_add', train_add, name='train_add_url'),
    path('carriage_add', carriage_add, name='carriage_add_url'),
    path('seat_add', seat_add, name='seat_add_url'),
    path('', buy, name='buy_url'),
    path('buy/<slug:reg_number>/<int:number>/', ticket_add, name="ticket_add_url"),
]