from django.shortcuts import render
from .models import Client, Lawyer, Deal, CurrentClient, Meeting, Payment
from .forms import ClientForm, ClientFormAuto, RegistrationForm, MeetingForm, PaymentForm
from django.views import generic


def index(request):
    current = CurrentClient.objects.get()
    return render(request, 'mainApp/main.html', {'current': current})


def contacts(request):
    current = CurrentClient.objects.get()
    return render(request, 'mainApp/contacts.html', {'current': current})


class DivorceListView(generic.ListView):
    model = Lawyer
    context_object_name = "context"
    queryset__in = Lawyer.objects.filter(type="d")
    template_name = "mainApp/types/divorce.html"


class AdviceListView(generic.ListView):
    model = Lawyer
    context_object_name = "context"
    queryset__in = Lawyer.objects.filter(type="a")
    template_name = "mainApp/types/advice.html"


class CrashListView(generic.ListView):
    model = Lawyer
    context_object_name = "context"
    queryset__in = Lawyer.objects.filter(type="c")
    template_name = "mainApp/types/crash.html"


def registration(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid() and Client.objects.exclude(passport=form.cleaned_data.get
            ('passport')):
            form.save()
            return render(request, 'mainApp/main.html')
        else:
            error = 'Incorrect form, try again.'

    form = ClientForm()
    context = {'form': form,
               'error': error
               }
    return render(request, 'mainApp/registration.html', context)


def authorisation(request):
    form = ClientFormAuto(request.POST)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            client = Client.objects.get(passport=form.cleaned_data.get('passport'))
            if client:
                CurrentClient.objects.all().delete()
                current = CurrentClient(
                    name=client.name,
                    passport=client.passport,
                    phone=client.phone
                )
                current.save()
                return index(request)
            else:
                error = 'Incorrect data, try again.'
    form = ClientFormAuto()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'mainApp/authorisation.html', context)


def exit(request):
    CurrentClient.objects.all().delete()
    current = CurrentClient(name=" ", passport=1, phone=1)
    current.save()
    return index(request)


def profile(request):
    prof = CurrentClient.objects.get()
    return render(request, 'mainApp/profile.html', {'profile': prof})


def start(request):
    form = RegistrationForm(request.POST)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            client = CurrentClient.objects.get()
            cl = Client.objects.get(passport=client.passport)
            deal = Deal(
                client=cl, lawyer=form.cleaned_data.get("lawyer"),
                date_opened=form.cleaned_data.get('date_opened'),
                date_closed=form.cleaned_data.get('date_closed'),
                status_lawyer="b"
            )
            deal.save()
            return index(request)
        else:
            error = 'Incorrect data, try again'
    form = RegistrationForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainApp/reg_deal.html', context)


def start_meeting(request):
    form = MeetingForm(request.POST)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            client = CurrentClient.objects.get()
            cl = Client.objects.get(passport=client.passport)
            meet = Meeting(
                client=cl, lawyer=form.cleaned_data.get("lawyer"),
                date=form.cleaned_data.get('date'),
                status_deal="n"
            )
            meet.save()
            return index(request)
        else:
            error = 'Incorrect data, try again'
    form = MeetingForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainApp/reg_meet.html', context)


def start_pay(request):
    form = PaymentForm(request.POST)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            client = CurrentClient.objects.get()
            cl = Client.objects.get(passport=client.passport)
            pay = Payment(
                client=cl, lawyer=form.cleaned_data.get("lawyer"),
                date=form.cleaned_data.get('date'), pay_sum=form.cleaned_data.get('pay_sum')
            )
            pay.save()
            return index(request)
        else:
            error = 'Incorrect data, try again'
    form = PaymentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainApp/reg_pay.html', context)

# Create your views here.
