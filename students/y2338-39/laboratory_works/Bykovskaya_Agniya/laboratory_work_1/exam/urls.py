from django.urls import path
from . import views

urlpatterns = [
    path("discipline/", views.DisciplineViewSet.as_view({'get': 'list'})),
    path("discipline/<int:pk>/", views.DisciplineViewSet.as_view({'get': 'retrieve'})),
    path("student/", views.StudentViewSet.as_view({'get': 'list'})),
    path("student/<int:pk>/", views.StudentViewSet.as_view({'get': 'retrieve'})),
    path("teacher/", views.TeacherViewSet.as_view({'get': 'list'})),
    path("teacher/<int:pk>/", views.TeacherViewSet.as_view({'get': 'retrieve'})),
    path("exam_schedule/", views.ExamScheduleViewSet.as_view({'get': 'list'})),
    path("exam_schedule/<int:pk>/", views.ExamScheduleViewSet.as_view({'get': 'retrieve'})),
    path("exam_schedule/create", views.ExamScheduleViewSet.as_view({'post': 'create'})),
    path("exam_schedule/<int:pk>/delete", views.ExamScheduleViewSet.as_view({'delete': 'destroy'})),
    path("exam/", views.ExamViewSet.as_view({'get': 'list'})),
    path("exam/<int:pk>/", views.ExamViewSet.as_view({'get': 'retrieve'})),
    path("exam/create", views.ExamViewSet.as_view({'post': 'create'})),
    path("exam/<int:pk>/delete", views.ExamViewSet.as_view({'delete': 'destroy'})),
    path("exam/<int:pk>/update", views.ExamViewSet.as_view({'post': 'update'})),


]