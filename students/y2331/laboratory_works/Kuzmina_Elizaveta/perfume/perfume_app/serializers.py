from rest_framework import serializers
from perfume_app.models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class BrokerSerializers(serializers.ModelSerializer):
    broker = UserSerializers()

    class Meta:
        model = Broker
        fields = ("id", "first_name", "second_name", "address", "birthdate", "broker")


class FirmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ("id", "name_firm", "country", "legal_address", "type_firm")


class DealSerializers(serializers.ModelSerializer):
    broker = BrokerSerializers()
    buyer = FirmSerializers()
    seller = FirmSerializers()

    class Meta:
        model = Deal
        fields = ("id", "date_deal", "broker", "buyer", "seller")


class DealCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ("date_deal", "buyer", "seller")


class FabricatorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fabricator
        fields = ("id", "name_fabricator", "country", "legal_address")


class ProductSerializers(serializers.ModelSerializer):
    fabricator = FabricatorSerializers()

    class Meta:
        model = Product
        fields = ("id", "name", "type", "shelf_life", "sex", "fabricator")


class ProductCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "type", "shelf_life", "sex", "fabricator")


class OrderDealSerializers(serializers.ModelSerializer):
    product = ProductSerializers()

    class Meta:
        model = OrderDeal
        fields = ("id", "deal", "product", "number_sold", "cost_seller", "cost_broker")