from django.contrib.auth import authenticate, login
from django.http import Http404
from django.contrib.auth.models import Group
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *


def base(request):
    return render(request, 'base.html')


def signup_job_seeker(request):
    if request.method == 'POST':
        form = Job_seeker_form(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.save()
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=my_password)
            login(request, user)
            return redirect('index')
    else:
        form = Job_seeker_form()
        return render(request, 'signup.html', {'form': form})


def signup_employer(request):
    # if request.method == 'POST':
    #     form = Employer_form(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         user.refresh_from_db()
    #         user.profile.name = form.cleaned_data.get('name')
    #         user.profile.email = form.cleaned_data.get('email')
    #         user.profile.phone_number = form.cleaned_data.get('phone_number')
    #         my_group = Group.objects.get(name='')
    #         my_group.user_set.add(user)
    #         user.save()
    #         my_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=user.username, password=my_password)
    #         login(request, user)
    #         return redirect('index')
    # else:
    form = Employer_form()
    return render(request, 'signup.html', {'form': form})

def signup2(request):
    return render(request, 'signup2.html')


def summary(request):
    context = {"dataset": Summary.objects.all()}
    return render(request, 'summary.html', context)


def vacancy(request):
    context = {"dataset": Vacancy.objects.all()}
    return render(request, 'vacancy.html', context)


def account(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        context = {'data_u': user, 'data_j': Job_seeker.objects.all(), 'data_s': Summary.objects.all(),
                   'data_e': Employer.objects.all(), 'data_v': Vacancy.objects.all()}
    except User.DoesNotExist:
        raise Http404("Пользователя не сущеcтвует")
    return render(request, 'account.html', context)


def vacancy_add(request, user_id):
    context = {}
    form = Vacancy_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    context["user"] = User.objects.get(pk=user_id)
    context["data_e"] = Employer.objects.all()
    return render(request, "vacancy_add.html", context)


def summary_add(request, user_id):
    context = {}
    form = Summary_form(request.POST or None)
    context['data_c'] = Summary.objects.all()
    if form.is_valid():
        form.save()
    context['form'] = form
    #context['data_j'] = Job_seeker.objects.get(pk=user_id)
    return render(request, "summary_add.html", context)


def signup(request):
    if request.method == 'POST':
        form = Job_seeker_form(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.email = form.cleaned_data.get('email')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.save()
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=my_password)
            login(request, user)
            return redirect('index')
        else:
            return  Http404("Пользователя не сущеcтвует")
    else:
        form = Job_seeker_form()
        return render(request, 'signup.html', {'form': form})


def summary_delete(request, summary_id):
    try:
        c = Summary.objects.get(id=summary_id)
        c.delete()
        context = {"dataset": Summary.objects.all()}
        return render(request, 'summary.html', context)
    except Summary.DoesNotExist:
        return HttpResponseNotFound("<h2>Резюме не найдено</h2>")


def vacancy_delete(request, vacancy_id):
    try:
        c = Vacancy.objects.get(id=vacancy_id)
        c.delete()
        context = {"dataset": Vacancy.objects.all()}
        return render(request, 'vacancy.html', context)
    except Vacancy.DoesNotExist:
        return HttpResponseNotFound("<h2>Вакансия не найдена</h2>")


def response(request, vacancy_id, user_id):
    context = {}
    form = Response_form(request.POST or None)
    if form.is_valid():
        form.save()
    context["data_v"] = Vacancy.objects.get(pk=vacancy_id)
    context['data_s'] = Summary.objects.all()
    context["user"] = User.objects.get(pk=user_id)
    context["data_e"] = Employer.objects.all(),
    context['form'] = form
    return render(request, "response.html", context)
# Create your views here.
