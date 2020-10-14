from django.urls import path
from . import views

urlpatterns = [
    path("patrolman/", views.output_patrolman, name='output_patrolman'),
    path("", views.output_patrol_result, name='output_patrol_result'),
    path("createPatrol/", views.create_patrol, name='create_patrol'),
    path("createWaterArea/", views.createWaterArea, name='createWaterArea'),
    path("profile/<int:pk>", views.output_profile, name='output_profile'),
    path("editprofile/<int:pk>", views.editPatrolman, name='editprofile'),
]