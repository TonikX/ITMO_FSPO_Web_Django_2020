from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('group/', views.GroupListView.as_view(), name='group-list'),
    path('group/<int:pk>/', views.GroupDetailView.as_view(), name='group-detail'),
    path('teacher/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('subject/<int:pk>/', views.SubjectDetailView.as_view(), name='subject-detail'),
    path('lesson/new/', views.LessonCreateView.as_view(), name='lesson-new'),
    path('lesson/<int:lesson_id>/', views.give_a_lesson, name='lesson-detail'),

    path('', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]