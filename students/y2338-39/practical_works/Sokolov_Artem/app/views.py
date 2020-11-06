from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from .models import Animal, Ticket, SalesHistory
from django.contrib import messages
from datetime import date

def index(request):
    animals = Animal.objects.all()
    form = SignUpForm()

    is_authorized = request.user.is_authenticated

    context = {
        'animals': animals,
        'is_user_logged_in': is_authorized,
        'registration_form': form
    }

    if is_authorized:
        tickets = Ticket.objects.all()
        context.update({
            'tickets': tickets
        })

    return render(request, 'app/home.html', context)

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            authenticate(request)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        else:
            messages.add_message(request, messages.ERROR, 'Возникла ошибка при регистрации')

        return redirect('index')

def buy_ticket(request):
    if request.method == 'POST':
        ticket_id = request.POST['ticket']

        if ticket_id:
            ticket = Ticket.objects.get(id=ticket_id)

            if not ticket:
                messages.add_message(request, messages.ERROR, 'Билет не найден')
            else:
                history = SalesHistory()
                history.date = date.today()
                history.ticket = ticket

                messages.add_message(request, messages.SUCCESS, 'Билет успешно куплен')

        return redirect('index')
