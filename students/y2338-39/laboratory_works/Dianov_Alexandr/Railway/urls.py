from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', station, name='station_url'),
    path('schedules_list/', schedules_list, name='schedules_list_url'),
    path('schedules_list/create',ScheduleCreate.as_view(), name='schedules_create_url'),
    path('train_list/',train_list, name='train_list_url'),
    path('train_list/create/',TrainCreate.as_view(), name='train_create_url'),
    path('schedules_list/update/', schedule_update_list, name='schedules_update_list_url'),
    path('schedules_list/update/<int:pk>', ScheduleUpdate.as_view(), name='schedules_update_url'),
    path('schedules_list/delete/', schedule_delete_list , name='schedules_delete_list_url'),
    path('schedules_list/delete/<int:pk>',ScheduleDelete.as_view(), name='schedules_delete_url'),
    path('train_list/update',train_update_list, name='train_update_list'),
    path('train_list/update/<int:pk>',TrainUpdate.as_view(), name='train_update'),
    path('train_list/delete/',train_delete_list, name='train_delete_list'),
    path('train_list/delete/<int:pk>',TrainDelete.as_view(), name='train_delete'),
    path('Auth/', AuthUser.as_view(), name='authentication'),
    path('Reg/', RegisterOfUser.as_view(), name='registration'),
    path('Auth/None', station, name='none_auth_log'),
]






