from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from django.views.generic import View, CreateView
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

def station(request):
    return render(request, 'Railway/ContactBlock.html')


def authen(request):
    return render(request, 'AuthForm.html')

def schedules_list(request):
    sch = Schedule.objects.all()
    return render(request, 'Railway/schedule.html', context={'Schedules': sch})


def train_list(request):
    trn = Train.objects.all()
    return render(request, 'Railway/trains.html', context={'Trains': trn})

@login_required()
def train_update_list(request):
    trn = Train.objects.all()
    return render(request,'Railway/Tr_update_list.html',context={'Trains': trn})

@login_required()
def train_delete_list(request):
    trn = Train.objects.all()
    return render(request,'Railway/Tr_delete_list.html',context={'Trains': trn})

@login_required()
def schedule_update_list(request):
    sch = Schedule.objects.all()
    return render(request, 'Railway/SchUpdate.html', context={'Schedules': sch})


@login_required()
def schedule_delete_list(request):
    sch = Schedule.objects.all()
    return render(request, 'Railway/SchDelete.html', context={'Schedules': sch})



class ScheduleCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        form = ScheduleForm()
        return render(request, 'Railway/SchCreate.html', context={'form': form})

    def post(self, request):
        form = ScheduleForm(request.POST)
        if (form.is_valid()):
            newSch = form.save()
            form = ScheduleForm()
            return render(request, 'Railway/SchCreate.html', context={'form': form})
        return render(request, 'Railway/SchCreate.html', context={'form': form})


class ScheduleUpdate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, pk):
        schd = Schedule.objects.get(RideId=pk)
        form = ScheduleForm(instance=schd)
        return render(request, 'Railway/SchTblUpdate.html', context={'form': form, 'schd': schd})

    def post(self, request, pk):
        schd = Schedule.objects.get(RideId=pk)
        form = ScheduleForm(request.POST, instance=schd)

        if (form.is_valid()):
            new = form.save(commit=False)
            new.save()
            sch = Schedule.objects.all()
            return redirect(reverse('schedules_list_url'))
        return render(request, 'Railway/SchTblUpdate.html', context={'form': form, 'schd': schd})


class ScheduleDelete(LoginRequiredMixin, View):
    def get(self, request, pk):
        sch = Schedule.objects.get(RideId=pk)
        return render(request, 'Railway/SchTblDelete.html', context={'sch': sch})

    def post(self,request,pk):
        sch = Schedule.objects.get(RideId=pk)
        sch.delete()
        return redirect(reverse('schedules_list_url'))

class TrainCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        form = TrainForm
        return render(request, 'Railway/TrCreate.html', context={'form': form})

    def post(self, request):
        form = TrainForm(request.POST)

        if (form.is_valid()):
            newSch = form.save()
            form = TrainForm
            return render(request, 'Railway/TrCreate.html', context={'form': form})
        return render(request, 'Railway/TrCreate.html', context={'form': form})
    # Create your views here.


class TrainUpdate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, pk):
        trn = Train.objects.get(Train_ID=pk)
        form = TrainForm(instance=trn)
        return render(request, 'Railway/Tr_update.html', context={'trn': trn,'form':form})

    def post(self, request, pk):
        trn = Train.objects.get(Train_ID=pk)
        form = TrainForm(request.POST,instance=trn)
        if (form.is_valid()):
            newSch = form.save(commit=False)
            newSch.save()
            return redirect(reverse('train_list_url'))
            #return render(request, 'Railway/TrCreate.html', context={'form': form})
        return render(request, 'Railway/Tr_update.html', context={'trn': trn, 'form': form})
    # Create your views here.


class TrainDelete(LoginRequiredMixin, View):
    def get(self, request, pk):
        trn = Train.objects.get(Train_ID=pk)
        return render(request, 'Railway/Tr_delete.html', context={'trn': trn})

    def post(self,request,pk):
        trn = Train.objects.get(Train_ID=pk)
        trn.delete()
        return redirect(reverse('train_list_url'))


class AuthUser(LoginView):
    template_name = 'AuthForm.html'
    form_class = AuthUserForm
    success_url_ = reverse_lazy('station_url')

    def get_success_url(self):
        return self.success_url

class RegisterOfUser(CreateView):
    model = User
    template_name = 'RegForm.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('station_url')
    success_msg = 'Successful'
