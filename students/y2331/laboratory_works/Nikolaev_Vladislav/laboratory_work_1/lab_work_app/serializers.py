from rest_framework import serializers
from lab_work_app.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username")


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ("routeName", "startCity", "finishCity", "distance")


class RouteNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ("id", "routeName")

class BusNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = ("id", "busNumber")

class BusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = ("busName", "mileage", "busType", "busNumber")


class RaceSerializer(serializers.ModelSerializer):
    raceBus = BusNumberSerializer()
    raceRoute = RouteNameSerializer()

    class Meta:
        model = Race
        fields = ("dateStart", "dateFinish", "amount", "price", "state", "raceRoute", "raceBus")


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ("user", "fullName", "location", "birth_date", "position", "contacts")


class DriversSerializer(serializers.ModelSerializer):
    person = ProfileSerializer()
    driverBus = BusNumberSerializer()

    class Meta:
        model = Drivers
        fields = ("person", "experience", "category", "driverBus")


# class DriversPostSerializer(serializers.ModelSerializer):
#     person = ProfileSerializer()
#
#     class Meta:
#         model = Drivers
#         fields = ("person", "experience", "category", "driverBus")
