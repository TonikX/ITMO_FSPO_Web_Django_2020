from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'price', 'pk']
        # read_only_fields=fields


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['car', 'time', 'transaction']
