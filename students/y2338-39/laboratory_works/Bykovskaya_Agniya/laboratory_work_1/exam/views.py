from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets, renderers
from django_filters.rest_framework import DjangoFilterBackend

from .service import StudentFilter, TeacherFilter
from .models import Discipline, Student, Teacher, ExamSchedule, Exam
from .serializers import DisciplineSerializer, StudentSerializer, TeacherSerializer, ExamScheduleSerializer, \
    ExamSerializer, ExamCreateSerializer, ExamScheduleCreateSerializer


class DisciplineViewSet(viewsets.ModelViewSet):
    """Отображение для модели Дисциплина"""
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """Отображение для модели Студент"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend,
                      )
    filterset_class = StudentFilter


class TeacherViewSet(viewsets.ModelViewSet):
    """Отображение для модели Преподаватель"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = (DjangoFilterBackend,
                       )
    filterset_class = TeacherFilter


class ExamScheduleViewSet(viewsets.ModelViewSet):
    """Отображение для модели Расписание"""
    queryset = ExamSchedule.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ExamScheduleCreateSerializer
        elif self.action == 'update':
            return ExamScheduleCreateSerializer
        else:
            return ExamScheduleSerializer



class ExamViewSet(viewsets.ModelViewSet):
    """Отображение для модели Экзамен"""
    queryset = Exam.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ExamCreateSerializer
        elif self.action == 'update':
            return ExamCreateSerializer
        else:
            return ExamSerializer