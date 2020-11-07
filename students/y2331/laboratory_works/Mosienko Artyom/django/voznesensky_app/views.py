from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from voznesensky_app.serializers import *


class ClientView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, pk=None):
        if pk:
            saved_client = get_object_or_404(Client.objects.all(), pk=pk)
            client = ClientSerializer(instance=saved_client)
            return Response(client.data, status=200)
        else:
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            return Response({"clients": serializer.data})

    def post(self, request):
        client = ClientSerializer(data=request.data)
        if client.is_valid():
            client.save()
            return Response({"success":True}, status=201)
        else:
            return Response({"success":False}, status=400)

    def put(self, request, pk):
        saved_client = get_object_or_404(Client.objects.all(), pk=pk)
        data = request.data
        client = ClientSerializer(instance=saved_client, data=data, partial=True)
        if client.is_valid():
            client.save()
            return Response({"success":True}, status=201)
        else:
            return Response({"success":False}, status=400)

    def delete(self, request, pk):
        client = get_object_or_404(Client.objects.all(), pk=pk)
        client.delete()
        return Response(status=204)

class TransactionView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, pk=None):
        if pk:
            saved_transaction = get_object_or_404(Transaction.objects.all(), pk=pk)
            transaction = TransactionSerializer(instance=saved_transaction)
            return Response(transaction.data, status=200)
        else:
            transactions = Transaction.objects.all()
            serializer = TransactionSerializer(transactions, many=True)
            return Response({"transactions": serializer.data})

    def post(self, request):
        transaction = TransactionSerializer(data=request.data)
        if transaction.is_valid():
            transaction.save()
            return Response({"success":True}, status=201)
        else:
            return Response({"success":False}, status=400)

    def put(self, request, pk):
        saved_transaction = get_object_or_404(Transaction.objects.all(), pk=pk)
        data = request.data
        transaction = TransactionSerializer(instance=saved_transaction, data=data, partial=True)
        if transaction.is_valid():
            transaction.save()
            return Response({"success":True}, status=201)
        else:
            return Response({"success":False}, status=400)

    def delete(self, request, pk):
        transaction = get_object_or_404(Transaction.objects.all(), pk=pk)
        transaction.delete()
        return Response(status=204)