from datetime import date

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.db.models import ObjectDoesNotExist

from . import models
from .forms import UserRegisterForm


# Create your views here.
def index(request):
    return render(request, 'base.html')


@login_required()
def profile(request):
    context = {}
    if request.user.is_teacher:
        context['lessons'] = models.Lesson.objects.filter(teacher=request.user).filter(date=date.today())
    else:
        context['lessons'] = models.Lesson.objects.filter(group=request.user.group).filter(date=date.today())
        for lesson in context['lessons']:
            try:
                lesson.grade = models.Grade.objects.get(student=request.user, lesson=lesson)
            except models.Grade.DoesNotExist:
                pass
    if request.user.is_teacher:
        subjects = models.Schedule.objects.filter(teacher=request.user).values_list('subject', flat=True).distinct()
    else:
        subjects = models.Schedule.objects.filter(group=request.user.group).values_list('subject', flat=True).distinct()
    context['subjects'] = []
    for sub_id in subjects:
        context['subjects'].append(models.Subject.objects.get(id=sub_id))

    return render(request, 'auth/profile.html', context)


@user_passes_test(lambda user: user.is_staff)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('profile')
        print(form.errors)
        return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})


@login_required()
@user_passes_test(lambda user: user.is_teacher)
def give_a_lesson(request, lesson_id):
    lesson = get_object_or_404(models.Lesson, id=lesson_id)
    if lesson.teacher != request.user:
        return HttpResponseForbidden
    students = models.Person.objects.filter(group=lesson.group)
    if request.method == 'POST':
        students_grade = request.POST.getlist('student_grade')
        for student, grade in zip(students, students_grade):
            if grade != '':
                grade = int(grade)
                if 1 < grade <= 5:
                    m_grade, created = models.Grade.objects.get_or_create(lesson=lesson, student=student,
                                                                          defaults={'grade': 1})
                    m_grade.grade = grade
                    m_grade.save()
        return redirect('subject-detail', lesson.subject.id)
    for student in students:
        try:
            student.grade = models.Grade.objects.get(lesson=lesson, student=student)
        except models.Grade.DoesNotExist:
            pass
    return render(request, 'schedule/give_a_lesson.html', {'students': students})


class LessonCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Lesson
    fields = ['group', 'subject', 'lesson_number']

    def test_func(self):
        return self.request.user.is_teacher

    def form_valid(self, form):
        form.instance.date = date.today()
        form.instance.teacher = self.request.user
        return super(LessonCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('lesson-detail', args=[self.object.id])


class GroupListView(LoginRequiredMixin, ListView):
    model = models.Group
    ordering = 'number'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GroupListView, self).get_context_data()
        context['teachers'] = models.Person.objects.filter(is_teacher=True)
        return context


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = models.Group

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data()
        all_schedule = models.Schedule.objects.filter(group=self.object)
        context['monday'] = all_schedule.filter(day='Mo').order_by('lesson_number')
        context['tuesday'] = all_schedule.filter(day='Tu').order_by('lesson_number')
        context['wednesday'] = all_schedule.filter(day='We').order_by('lesson_number')
        context['thursday'] = all_schedule.filter(day='Th').order_by('lesson_number')
        context['friday'] = all_schedule.filter(day='Fr').order_by('lesson_number')
        context['saturday'] = all_schedule.filter(day='Sa').order_by('lesson_number')
        return context


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = models.Person
    template_name = 'schedule/group_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherDetailView, self).get_context_data()
        all_schedule = models.Schedule.objects.filter(teacher=self.object)
        context['monday'] = all_schedule.filter(day='Mo').order_by('lesson_number')
        context['tuesday'] = all_schedule.filter(day='Tu').order_by('lesson_number')
        context['wednesday'] = all_schedule.filter(day='We').order_by('lesson_number')
        context['thursday'] = all_schedule.filter(day='Th').order_by('lesson_number')
        context['friday'] = all_schedule.filter(day='Fr').order_by('lesson_number')
        context['saturday'] = all_schedule.filter(day='Sa').order_by('lesson_number')
        return context


class SubjectDetailView(LoginRequiredMixin, DetailView):
    model = models.Subject

    def get_context_data(self, **kwargs):
        context = super(SubjectDetailView, self).get_context_data()
        if self.request.user.is_teacher:
            context['lessons'] = models.Lesson.objects.filter(teacher=self.request.user).filter(
                subject=self.object).order_by('-date')
        else:
            context['lessons'] = models.Lesson.objects.filter(group=self.request.user.group).filter(
                subject=self.object).order_by('-date')
            for lesson in context['lessons']:
                try:
                    lesson.grade = models.Grade.objects.get(student=self.request.user, lesson=lesson)
                except models.Grade.DoesNotExist:
                    pass

        if self.request.user.is_teacher:
            subjects = models.Schedule.objects.filter(teacher=self.request.user).values_list('subject',
                                                                                             flat=True).distinct()
        else:
            subjects = models.Schedule.objects.filter(group=self.request.user.group).values_list('subject',
                                                                                                 flat=True).distinct()
        context['subjects'] = []
        for sub_id in subjects:
            context['subjects'].append(models.Subject.objects.get(id=sub_id))
        return context
