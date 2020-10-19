from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, CreateView

import perfum.models


def index(request):
    return render(request, 'index.html')


class BrokerListView(ListView):
    model = perfum.models.Broker


class BrokerCreateView(CreateView):
    model = perfum.models.Broker
    fields = [
        'broker_name',
        'broker_addr',
        'broker_dob'
    ]
    labels = [
        {'broker_name': "New Broker's name: "},
        {'broker_addr': "New Broker's address: "},
        {'broker_dob': "New Broker's date of birth: "}
    ]
    success_url = 'succ'


def broker_detail(request, broker_id):
    try:
        p = perfum.models.Broker.objects.get(pk=broker_id)
    except perfum.models.Broker.DoesNotExist:
        raise Http404('This Broker does not exist')
    return render(request, 'perfum/broker_detail.html', {'Broker': p})


class BuyerListView(ListView):
    model = perfum.models.Buyer


class BuyerCreateView(CreateView):
    model = perfum.models.Buyer
    fields = [
        'buyer_name'
    ]
    labels = [
        {'buyer_name': "New Buyer's name: "}
    ]
    success_url = 'succ'


def buyer_detail(request, bid):
    try:
        p = perfum.models.Buyer.objects.get(pk=bid)
    except perfum.models.Buyer.DoesNotExist:
        raise Http404('This Buyer does not exist')
    return render(request, 'perfum/buyer_detail.html', {'Buyer': p})


class DealListView(ListView):
    model = perfum.models.Deal


class DealCreateView(CreateView):
    model = perfum.models.Deal
    fields = [
        'deal_date',
        'deal_sold',
        'fk_broker',
        'fk_product',
        'fk_buyer'
    ]
    labels = [
        {'deal_date': "New Deal date: "},
        {'deal_sold': "PCS Sold: "},
        {'fk_broker': "Broker ID: "},
        {'fk_product': "Product ID: "},
        {'fk_buyer': "Buyer ID: "}
    ]
    success_url = 'succ'


def deal_detail(request, deal_id):
    try:
        p = perfum.models.Deal.objects.get(pk=deal_id)
    except perfum.models.Deal.DoesNotExist:
        raise Http404('This Deal does not exist')
    return render(request, 'perfum/deal_detail.html', {'Deal': p})


class ProductListView(ListView):
    model = perfum.models.Product


def product_detail(request, product_id):
    try:
        p = perfum.models.Product.objects.get(pk=product_id)
    except perfum.models.Product.DoesNotExist:
        raise Http404('This Product does not exist')
    return render(request, 'perfum/product_detail.html', {'Product': p})


class ProductCreateView(CreateView):
    model = perfum.models.Product
    fields = [
        'product_name',
        'product_type',
        'product_best_before',
        'product_price',
        'product_in_stock',
        'fk_seller'
    ]
    success_url = 'succ'


class SellerListView(ListView):
    model = perfum.models.Seller


class SellerCreateView(CreateView):
    model = perfum.models.Seller
    fields = [
        'seller_name'
    ]
    success_url = 'succ'


def seller_detail(request, seller_id):
    try:
        p = perfum.models.Seller.objects.get(pk=seller_id)
    except perfum.models.Seller.DoesNotExist:
        raise Http404('This Seller does not exist')
    return render(request, 'perfum/seller_detail.html', {'Seller': p})
