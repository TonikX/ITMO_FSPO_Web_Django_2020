import datetime
import random

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import FormView

from .models import *


def toHomepage(request):
    if request.user.username == 'merchandiser':
        return HttpResponseRedirect("/admission/")
    else:
        return HttpResponseRedirect("/")


class RegisterView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


def catalog(request):
    if request.POST.get('btn_add', None) is not None:
        add_cassette(request.POST['cassette_id'], 1, request)
        return HttpResponseRedirect(request.path_info)
    if request.user.is_authenticated:
        order = get_order_or_create(request)
        cassettes_in_order = CassetteInOrder.objects.filter(order_id=order.id).values('cassette_id')
        cassettes = Cassette.objects.filter(~Q(id__in=cassettes_in_order))
    else:
        cassettes = Cassette.objects.all()
    return render(request, "cassettes.html", {"cassettes": cassettes})


def find_seller():
    sellers = Seller.objects.all()
    arr = []
    for seller in sellers:
        arr.append(seller.id)
    choice = random.choice(arr)
    return choice


def get_order_or_create(request):
    try:
        order = Order.objects.get(customer=request.user.id, bought=False)
    except:
        order = Order()
        order.customer = request.user.id
        order.seller = Seller.objects.get(pk=find_seller())
        order.save()
    return order


def add_cassette(cassette_id, count, request):
    order = get_order_or_create(request)
    try:
        cassette_in_order = CassetteInOrder.objects.get(cassette_id=cassette_id, order_id=order.id)
    except:
        cassette_in_order = CassetteInOrder()
        cassette_in_order.cassette = Cassette.objects.get(pk=cassette_id)
        cassette_in_order.order = order
        cassette_in_order.price = Cassette.objects.get(pk=cassette_id).price
    cassette_in_order.count = count
    cassette_in_order.save()
    return


def cart(request):
    if request.POST.get('btn_edit', None) is not None:
        add_cassette(request.POST['cassette_id'], int(request.POST['count']), request)
        return HttpResponseRedirect(request.path_info)
    if request.POST.get('btn_remove', None) is not None:
        remove_cassette(request.POST['cassette_id'], request)
        return HttpResponseRedirect(request.path_info)
    order = get_order_or_create(request)
    cassettes_in_order = CassetteInOrder.objects.filter(order_id=order.id).values('cassette_id')
    cassettes = Cassette.objects.filter(id__in=cassettes_in_order)
    sum_price = 0
    sum_count = 0
    for cassette in cassettes:
        cassette.selected_count = CassetteInOrder.objects.get(cassette_id=cassette.id, order_id=order.id).count
        sum_price += cassette.selected_count * cassette.price
        sum_count += cassette.selected_count
    if request.POST.get('btn_confirm', None) is not None:
        order.date = datetime.datetime.now()
        order.bought = True
        for cassette in cassettes:
            cassette.count = cassette.count - cassette.selected_count
            cassette.save()
        order.save()
        return HttpResponseRedirect(request.path_info)
    context = {
        'cassettes': cassettes,
        'sum_price': sum_price,
        'sum_count': sum_count,
    }
    return render(request, 'cart.html', context)


def remove_cassette(cassette_id, request):
    order = get_order_or_create(request)
    cassette_in_order = CassetteInOrder.objects.get(cassette_id=cassette_id, order_id=order.id)
    if cassette_in_order is not None:
        cassette_in_order.delete()
    return


def orders(request):
    c_orders = Order.objects.filter(customer=request.user.id, bought=True).order_by('-date')
    for order in c_orders:
        sum_price = 0
        sum_count = 0
        cassettes_in_order = CassetteInOrder.objects.filter(order=order).values('cassette_id')
        cassettes = Cassette.objects.filter(id__in=cassettes_in_order)
        order.cassettes = cassettes
        for cassette in cassettes:
            try:
                cassette_in_order = CassetteInOrder.objects.get(order_id=order, cassette_id=cassette.id)
                cassette.selected_count = cassette_in_order.count
                cassette.bought_price = cassette_in_order.price
                sum_price += cassette.selected_count * cassette.bought_price
                sum_count += cassette.selected_count
            except:
                cassette.selected_count = 0
        order.sum_price = sum_price
        order.sum_count = sum_count
    context = {
        'c_orders': c_orders,
    }
    return render(request, 'orders.html', context)


def admission(request):
    cassettes = Cassette.objects.all()
    context = {
        'cassettes': cassettes,
    }
    if request.POST.get('btn_add_cassette', None) is not None:
        try:
            add_admission = Admission()
            add_admission.cassette = Cassette.objects.get(title=request.POST['cassette_title'])
            add_admission.count = int(request.POST['count'])
            add_admission.date = datetime.datetime.now()
            add_admission.seller = Seller.objects.get(pk=find_seller())
            add_admission.save()

            cassette = Cassette.objects.get(title=request.POST['cassette_title'])
            cassette.count = cassette.count + int(request.POST['count'])
            cassette.save()
            return HttpResponseRedirect(request.path_info)
        except:
            return render(request, 'admission.html', context)
    return render(request, 'admission.html', context)


def getAdmissions(request):
    admissions = Admission.objects.all().order_by('-date')
    context = {
        'admissions': admissions,
    }
    return render(request, 'admissions.html', context)

