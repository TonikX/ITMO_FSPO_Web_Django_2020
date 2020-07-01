from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from lab_work_app.serializers import *


class RouteView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        rout = Route.objects.all()
        serializer = RouteSerializer(rout, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        client = RouteSerializer(data=request.data)
        if client.is_valid():
            client.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request):
        saved_client = get_object_or_404(Route.objects.all())
        data = request.data
        serializer = RouteSerializer(instance=saved_client, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request):
        client = get_object_or_404(Route.objects.all())
        client.delete()
        return Response(status=204)


class BusView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        bus = Bus.objects.all()
        serializer = BusSerializer(bus, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        client = BusSerializer(data=request.data)
        if client.is_valid():
            client.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request):
        saved_client = get_object_or_404(Bus.objects.all())
        data = request.data
        serializer = BusSerializer(instance=saved_client, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request):
        client = get_object_or_404(Bus.objects.all())
        client.delete()
        return Response(status=204)


class RaceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        race = Race.objects.all()
        serializer = RaceSerializer(race, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        client = RaceSerializer(data=request.data)
        if client.is_valid():
            client.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request):
        saved_client = get_object_or_404(Race.objects.all())
        data = request.data
        serializer = RaceSerializer(instance=saved_client, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request):
        client = get_object_or_404(Race.objects.all())
        client.delete()
        return Response(status=204)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        prof = Profile.objects.all()
        serializer = ProfileSerializer(prof, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        client = ProfileSerializer(data=request.data)
        if client.is_valid():
            client.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request):
        saved_client = get_object_or_404(Profile.objects.all())
        data = request.data
        serializer = ProfileSerializer(instance=saved_client, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request):
        client = get_object_or_404(Profile.objects.all())
        client.delete()
        return Response(status=204)


class DriversView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        drivers = Drivers.objects.all()
        serializer = DriversSerializer(drivers, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        client = DriversSerializer(data=request.data)
        if client.is_valid():
            client.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request):
        saved_client = get_object_or_404(Drivers.objects.all())
        data = request.data
        serializer = DriversSerializer(instance=saved_client, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request):
        client = get_object_or_404(Drivers.objects.all())
        client.delete()
        return Response(status=204)
