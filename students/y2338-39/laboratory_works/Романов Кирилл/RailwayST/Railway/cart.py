from django.conf import settings
from Railway.models import *


class Cart(object):

    def __init__(self,request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart :
            cart = self.session[settings.CART_SESSION_ID] ={}
        self.cart = cart

    def add(self,Ticket):
        tck = Ticket.Ticket_ID
        tck.save()
    def save(self):
        self.session.modified = True





