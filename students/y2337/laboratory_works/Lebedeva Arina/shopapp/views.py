from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic import View

from .models import *
from django.views.generic.edit import CreateView, UpdateView
from .forms import *


def game_list(request):
    game = Game.objects.all()
    return render(request, "game/game_list.html", {"game": game})


def game_single(request, pk):
    game = get_object_or_404(Game, id=pk)
    return render(request, "game/game_single.html", {"game": game})


class DeleteGame(View):
    def get(self, request, pk):
        object = get_object_or_404(Game, id=pk)
        return render(request, "delete.html", context={"object": object})

    def post(self, request, pk):
        object = get_object_or_404(Game, id=pk)
        object.delete()
        return redirect("game_list")


class AddGame(CreateView):
    model = Game
    form_class = AddGameForm
    template_name = "add.html"

    def form_valid(self, form):
        form.save()
        return redirect("game_list")


class UpdateGame(UpdateView):
    model = Game
    form_class = AddGameForm
    template_name = "add.html"

    def get_success_url(self):
        return reverse('game_list')


class AddDeveloper(CreateView):
    model = Developer
    form_class = AddDeveloperForms
    template_name = "add.html"

    def form_valid(self, form):
        form.save()
        return redirect("developer_list")


class UpdateDeveloper(UpdateView):
    model = Developer
    form_class = AddDeveloperForms
    template_name = "add.html"

    def get_success_url(self):
        return reverse('developer_list')


class ListDeveloper(ListView):
    model = Developer
    template_name = "developer/list.html"


class DeleteDeveloper(View):
    def get(self, request, pk):
        object = get_object_or_404(Developer, id=pk)
        return render(request, "delete.html", context={"object": object})

    def post(self, request, pk):
        object = get_object_or_404(Developer, id=pk)
        object.delete()
        return redirect("developer_list")


class AddCD(CreateView):
    model = CD
    form_class = AddCDForms
    template_name = "add.html/"

    def form_valid(self, form):
        form.save()
        return redirect("cd_list")


class UpdateCD(UpdateView):
    model = CD
    form_class = AddCDForms
    template_name = "add.html"

    def get_success_url(self):
        return reverse('cd_list')


class ListCD(ListView):
    model = CD
    template_name = "cd/cd_list.html"


class DeleteCD(View):
    def get(self, request, pk):
        object = get_object_or_404(CD, id=pk)
        return render(request, "delete.html", context={"object": object})

    def post(self, request, pk):
        object = get_object_or_404(CD, id=pk)
        object.delete()
        return redirect("cd_list")


class AddCustomer(CreateView):
    model = Customer
    form_class = AddCustomerForms
    template_name = "add.html/"

    def form_valid(self, form):
        form.save()
        return redirect("customer_list")


class UpdateCustomer(UpdateView):
    model = Customer
    form_class = AddCustomerForms
    template_name = "add.html"

    def get_success_url(self):
        return reverse('customer_list')


class ListCustomer(ListView):
    model = Customer
    template_name = "customer/list.html"


class DeleteCustomer(View):
    def get(self, request, pk):
        object = get_object_or_404(Customer, id=pk)
        return render(request, "delete.html", context={"object": object})

    def post(self, request, pk):
        object = get_object_or_404(Customer, id=pk)
        object.delete()
        return redirect("customer_list")


class AddOrder(CreateView):
    model = Order
    form_class = AddOrderForms
    template_name = "add.html/"

    def form_valid(self, form):
        form.save()
        return redirect("order_list")


class UpdateOrder(UpdateView):
    model = Order
    form_class = AddOrderForms
    template_name = "add.html"

    def get_success_url(self):
        return reverse('order_list')


class ListOrder(ListView):
    model = Order
    template_name = "order/list.html"


class DeleteOrder(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        return render(request, "delete.html", context={"object": order})

    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        order.delete()
        return redirect("order_list")