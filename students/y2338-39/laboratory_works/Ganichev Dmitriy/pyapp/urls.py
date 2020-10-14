from django.urls import path
from . import views


urlpatterns = [
    path('hunters/', views.HunterView.as_view()),
    path('hunters/<int:idx>', views.HuntersObjectView.as_view()),
    path('furpoints/', views.FurPointView.as_view()),
    path('furfactories/', views.FurFactoryView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('check/', views.UsernameCheckView.as_view()),
    path('me/', views.MeView.as_view()),
    path('me/data/', views.MeDataView.as_view()),
]
