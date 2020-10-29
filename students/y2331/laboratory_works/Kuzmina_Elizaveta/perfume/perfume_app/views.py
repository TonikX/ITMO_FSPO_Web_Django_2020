# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from django.db.models import Q
from perfume_app.models import *
from perfume_app.serializers import *


class BrokerView(APIView):
    """Просмотр маклеров"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        if request.user.is_superuser:
            brokers = Broker.objects.all()
            serializer = BrokerSerializers(brokers, many=True)
            return Response({"data": serializer.data})
        else:
            brokers = Broker.objects.filter(broker=request.user)
            serializer = BrokerSerializers(brokers, many=True)
            return Response({"data": serializer.data})


class FirmView(APIView):
    """Просмотр фирм"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        firms = Firm.objects.all()
        serializer = FirmSerializers(firms, many=True)
        return Response({"data": serializer.data})


class DealCRUDView(APIView):
    """CRUD сделок"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        if request.user.is_superuser:
            deals = Deal.objects.all()
            serializer = DealSerializers(deals, many=True)
            return Response({"data": serializer.data})
        else:
            broker = Broker.objects.filter(broker=request.user)
            deal = Deal.objects.filter(broker__in=broker)
            serializer = DealSerializers(deal, many=True)
            return Response({"data": serializer.data})

    def post(self, request):
        deal = DealCRUDSerializers(data=request.data)
        if deal.is_valid():
            broker_found = Broker.objects.get(broker=request.user)
            broker = get_object_or_404(Broker, id=broker_found.id)
            seller = get_object_or_404(Firm, id=self.request.data.get('seller'))
            buyer = get_object_or_404(Firm, id=self.request.data.get('buyer'))
            deal.save(broker=broker, seller=seller, buyer=buyer)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        saved_deal = get_object_or_404(Deal.objects.all(), pk=pk)
        serializer = DealCRUDSerializers(instance=saved_deal, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        deal = get_object_or_404(Deal.objects.all(), pk=pk)
        deal.delete()
        return Response(status=201)


class FabricatorView(APIView):
    """Просмотр производителей"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        fabricators = Fabricator.objects.all()
        serializer = FabricatorSerializers(fabricators, many=True)
        return Response({"data": serializer.data})


class ProductCRUDView(APIView):
    """CRUD товаров"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        fabricator = request.GET.get("fabricator")
        if fabricator == None:
            products = Product.objects.all()
            serializer = ProductSerializers(products, many=True)
            return Response({"data": serializer.data})
        else:
            product = Product.objects.filter(fabricator=fabricator)
            serializer = ProductSerializers(product, many=True)
            return Response({"data": serializer.data})

    def post(self, request):
        product = ProductCRUDSerializers(data=request.data)
        if product.is_valid():
            fabricator = get_object_or_404(Fabricator, id=self.request.data.get("fabricator"))
            product.save(fabricator=fabricator)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        saved_product = get_object_or_404(Product.objects.all(), pk=pk)
        serializer = ProductCRUDSerializers(instance=saved_product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response(status=201)


class OrderDealView(APIView):
    """Просмотр заказов сделки"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        deal = request.GET.get("deal", -1)
        if deal == -1:
            order_deals = OrderDeal.objects.all()
            serializer = OrderDealSerializers(order_deals, many=True)
            return Response({"data": serializer.data})
        else:
            order_deals = OrderDeal.objects.filter(deal=deal)
            serializer = OrderDealSerializers(order_deals, many=True)
            return Response({"data": serializer.data})
