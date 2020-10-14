from rest_framework import serializers
from .models import *


class AppUserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    role = serializers.CharField(source='get_role_display')

    def get_username(self, obj):
        return obj.user.username

    def get_id(self, obj):
        return obj.user.id

    class Meta:
        model = AppUser
        fields = ("id", "username", "role")


class HunterSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = AppUserSerializer()

    def get_id(self, obj):
        return obj.pk

    class Meta:
        model = Hunter
        fields = ('id', 'user', 'address')


class FurPointSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = AppUserSerializer()

    def get_id(self, obj):
        return obj.pk

    class Meta:
        model = FurPoint
        fields = ('id', 'user', 'address')


class FurFactorySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = AppUserSerializer()

    def get_id(self, obj):
        return obj.pk

    class Meta:
        model = FurFactory
        fields = ('id', 'user', 'name')


class FurGatherSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.pk

    class Meta:
        model = FurGathering
        fields = ('id', 'id_hunter', 'type', 'sort', 'count', 'date')


class FurShipmentSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.pk

    class Meta:
        model = FurShipment
        fields = ('id', 'id_furfactory', 'id_furpoint', 'type', 'sort', 'count', 'price', 'date')


class FurDeliverySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    def get_id(self, obj):
        return obj.pk

    class Meta:
        model = FurDelivery
        fields = ('id', 'id_furpoint', 'id_hunter', 'type', 'sort', 'count', 'price', 'date')
