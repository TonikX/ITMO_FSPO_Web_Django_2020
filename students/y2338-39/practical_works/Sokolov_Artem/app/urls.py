from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('buy_ticket', views.buy_ticket, name='buy_ticket'),
    url(r'^logout/$', LogoutView.as_view(), {'next': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^login/$', LoginView.as_view(), {'next': settings.LOGIN_REDIRECT_URL}, name='login')
]