from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from projectApp.forms import LoginForm, RegForm, VoyageForm, TrawlerForm, AssignForm, AwardForm, StockForm
from django.contrib.auth import authenticate, login
from projectApp.models import ExtendedUserModel, Voyage, Crews, Trawlers, Awards, FishOperation
import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.views.generic.edit import FormView as EditFormView
from django.views.generic.list import ListView


# Create your views here.


def voyage_view(request):
    return render(request, 'actions/voyage.html', context={})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/account/')

                else:
                    return render(request, 'registration/accSuspended.html', context={})
            else:
                return render(request, 'registration/badCred.html', context={})
        else:
            return HttpResponse('Invalid form')
    else:
        form = LoginForm()
    context = {}
    context['form'] = form
    return render(request, "registration/login.html", context)


def bad_credentials(request):
    return render(request, 'registration/badCred.html', context={})


def register_view(request):
    if request.method == 'POST':
        form = RegForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            if data['password'] == data['password_confirmation']:
                username_check = ExtendedUserModel.objects.filter(username=data['username']).count()
                if username_check == 0:
                    user = ExtendedUserModel.objects.create(username=data['username'],
                                                            first_name=data['first_name'],
                                                            last_name=data['last_name'],
                                                            b_day=data['b_day'],
                                                            password=make_password(data['password']),
                                                            last_login=None,
                                                            job_type=data['job_type'],
                                                            hire_date=datetime.datetime.now())
                    if user._meta.get_field('job_type').value_from_object(user) == 'ACC':
                        ass_group = Group.objects.get(name='Accountants')
                        ass_group.user_set.add(user)
                    elif user._meta.get_field('job_type').value_from_object(user) == 'SLR':
                        ass_group = Group.objects.get(name='Sailors')
                        ass_group.user_set.add(user)
                    elif user._meta.get_field('job_type').value_from_object(user) == 'CPT':
                        ass_group = Group.objects.get(name='Captains')
                        ass_group.user_set.add(user)

                    login(request, user)
                    return HttpResponseRedirect('/account/')
                else:
                    return HttpResponse('Username already taken.')
            else:
                return HttpResponse("Passwords don't match.")

        else:
            return HttpResponse('Invalid form')
    else:
        form = RegForm()
    context = {'form': form}
    return render(request, "registration/register.html", context)


def user_view(request):
    if request.user._meta.get_field('job_type').value_from_object(request.user) == 'ACC':
        context = {'voyage_list': Voyage.objects.all().order_by('id')[:10],
                   'trawler_list': Trawlers.objects.all().order_by('id')[:10],
                   'sop_list': FishOperation.objects.all().order_by('id')[:10]}
        return render(request, 'account/accountant.html', context)
    elif request.user._meta.get_field('job_type').value_from_object(request.user) == 'SLR' or \
            request.user._meta.get_field('job_type').value_from_object(request.user) == 'CPT':

        context = {}
        if request.user._meta.get_field('job_type').value_from_object(request.user) == 'CPT':
            context['cap'] = True
            context['job'] = 'captain'
        else:
            context['job'] = 'sailor'
        print(context)
        if not Crews.objects.filter(uId=request.user.id).count() == 0:
            crew = Crews.objects.get(uId=request.user.id)
            context['trwlr'] = "You are assigned to " + crew.tId.name
            if not Voyage.objects.filter(tId=crew.tId).count() == 0:
                context['voyage_list'] = Voyage.objects.filter(tId=crew.tId).order_by('id')[:10]
        else:
            context['trwlr'] = "You are currently not assigned to any ship"

        if not Awards.objects.filter(uId=request.user.id).count() == 0:
            context['awards_list'] = Awards.objects.filter(uId=request.user.id).order_by('id')[:10]
        print(context)
        return render(request, 'account/sailor.html', context)

    else:
        return HttpResponseRedirect('/admin/')


def new_voyage_view(request):
    if request.user.has_perm('projectApp.add_voyage'):
        if request.method == 'POST':
            form = VoyageForm(request.POST or None)
            if form.is_valid():
                data = form.cleaned_data
                if not data['startDate'] > data['endDate']:
                    if not Crews.objects.filter(uId=request.user.id).count() == 0:
                        Voyage.objects.create(startDate=data['startDate'],
                                              endDate=data['endDate'],
                                              tId=Crews.objects.get(uId=request.user.id).tId,
                                              fishQty=data['fishQty'])
                        return HttpResponseRedirect('/account/')
                    else:
                        return HttpResponse('<p>You are currently not assigned to any ship.</p><a href="/account">Go back</a>')
                else:
                    return HttpResponse('Start date must be less that end date.')
            else:
                return HttpResponse('Invalid form')
        else:
            form = VoyageForm()
            context = {'form': form}
            return render(request, "actions/addvoyage.html", context)
    else:
        return render(request, 'noperm.html', context={})


class AssignView(EditFormView):
    template_name = 'actions/ass_crew.html'
    form_class = Crews

    fields = ['tId', 'uId']


def new_trawler_view(request):
    if request.user.has_perm('projectApp.edit_ship_info'):
        if request.method == 'POST':
            form = TrawlerForm(request.POST or None)
            if form.is_valid():
                data = form.cleaned_data
                print(data)
                Trawlers.objects.create(name=data['name'],
                                        prodDate=data['prodDate'])
                return HttpResponseRedirect('/account/')
            else:
                return HttpResponse('Invalid form')
        else:
            form = TrawlerForm()
            context = {'form': form}
            return render(request, "actions/addtrawler.html", context)
    else:
        return render(request, 'noperm.html', context={})


def trawler_view(request):
    return render(request, 'actions/trawler.html', context={})


def assign_view(request):
    if request.user.has_perm('projectApp.edit_crews'):
        if request.method == 'POST':
            form = AssignForm(request.POST or None)
            if form.is_valid():
                data = form.cleaned_data
                print(data)
                Crews.objects.create(uId=data['uId'],
                                     tId=data['tId'])
                return HttpResponseRedirect('/account/')
            else:
                return HttpResponse('Invalid form')
        else:
            form = AssignForm()
            sett = ExtendedUserModel.objects.filter(is_superuser=False)
            sett = sett.exclude(job_type='ACC')
            form.fields['uId'].queryset = sett.exclude()
            context = {'form': form}
            return render(request, "actions/ass_crew.html", context)
    else:
        return render(request, 'noperm.html', context={})


def award_view(request):
    if request.user.has_perm('projectApp.see_award'):
        if request.method == 'POST':
            form = AwardForm(request.POST or None)
            if form.is_valid():
                data = form.cleaned_data
                Awards.objects.create(uId=data['uId'],
                                      date=datetime.datetime.now(),
                                      awardSize=data['awardSize'])
                return HttpResponseRedirect('/account/')
            else:
                return HttpResponse('Invalid form')
        else:
            form = AwardForm()
            sett = ExtendedUserModel.objects.filter(is_superuser=False)
            sett = sett.exclude(job_type='ACC')
            form.fields['uId'].queryset = sett.exclude()
            context = {'form': form}
            return render(request, "actions/addaward.html", context)
    else:
        return render(request, 'noperm.html', context={})


def operation_view(request):
    if request.user.has_perm('projectApp.see_fish_op'):
        if request.method == 'POST':
            form = StockForm(request.POST or None)
            if form.is_valid():
                data = form.cleaned_data
                FishOperation.objects.create(price=data['price'],
                                      date=data['date'])
                return HttpResponseRedirect('/account/')
            else:
                return HttpResponse('Invalid form')
        else:
            form = StockForm()
            context = {'form': form}
            return render(request, "actions/addfop.html", context)
    else:
        return render(request, 'noperm.html', context={})


# TODO сделать функциональную часть для всех пользователей
