from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View
from django.http import HttpResponseRedirect
from .mixins import *
from django.contrib import messages
from .forms import OrderForm
from .utils import *


def genres_list(request):
    genres = Genre.objects.all()
    return render(request, "genre_list.html", context={"genre_list": genres})


def games_list(request):
    games = Game.objects.all()
    return render(request, "game_list.html", context={"game_list": games})


class GameDetail(View):

    def get(self, request, game_id):
        game = get_object_or_404(Game, pk=game_id)
        return render(request, "game_detail.html", context={"game": game})


class GenreDetail(View):

    def get(self, request, genre_id):
        genre = get_object_or_404(Genre, pk=genre_id)
        return render(request, "genre_detail.html", context={"genre": genre})


class CartView(CartMixin, View):

    def get(self, request):
        return render(request, "cart.html", context= {'cart': self.cart})


class AddToCart(CartMixin, View):

    def get(self, request, game_id):
        game = get_object_or_404(Game, pk=game_id)
        cart_game, created = CartGame.objects.get_or_create(owner=self.customer, cart=self.cart, game=game, final_price= game.price)
        if created:
            self.cart.games.add(cart_game)
            recalc_cart(self.cart)
            messages.add_message(request, messages.INFO, "Товар успешно добавлен")
        return HttpResponseRedirect('/cart/')


class RemoveFromCart(CartMixin, View):

    def get(self, request, game_id):
        game = get_object_or_404(Game, pk=game_id)
        cart_game = CartGame.objects.get(owner=self.customer, cart=self.cart, game=game)
        self.cart.games.remove(cart_game)
        CartGame.delete(cart_game)
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Товар успешно удален")
        return HttpResponseRedirect('/cart/')


class ChangeQTYView(CartMixin, View):

    def post(self, request, game_id):
        game = get_object_or_404(Game, pk=game_id)
        cart_game = CartGame.objects.get(owner=self.customer, cart=self.cart, game=game)
        qty = int(request.POST.get('qty'))
        cart_game.qty = qty
        cart_game.save()
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Кол-во успешно изменено")
        return HttpResponseRedirect('/cart/')


class Checkout(CartMixin, View):

    def get(self, request):
        form = OrderForm(request.POST or None)
        return render(request, "checkout.html", context= {'cart': self.cart, "form": form})


class MakeOrderView(CartMixin, View):

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = self.customer
            new_order.first_name = form.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.email = form.cleaned_data['email']
            new_order.save()
            self.cart.in_order = True
            new_order.cart = self.cart
            new_order.save()
            self.customer.orders.add(new_order)
            messages.add_message(request, messages.INFO, 'Спасибо за заказ, мендежер с Вами свяжется')
            self.cart.delete()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/checkout/')



