from django.forms import ModelForm
from .models import Flight, Heli, Ticket, Pilot


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('category',)



