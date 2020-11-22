from django.contrib import admin
from .models import Discipline, Student, Teacher, ExamSchedule, Exam

admin.site.register(Discipline)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(ExamSchedule)
admin.site.register(Exam)