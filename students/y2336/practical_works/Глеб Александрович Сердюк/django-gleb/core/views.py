from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import models
from .forms import UserRegisterForm


# Create your views here.
def index(request):
    return render(request, 'base.html')


@login_required()
def add_item_to_shopping_bag(request, item_id):
    item = get_object_or_404(models.Jewelry, id=item_id)
    models.ProductInShoppingBag.objects.create(product=item, client=request.user)
    return redirect('jewelry-detail', item_id)


@login_required()
def delete_item_from_shopping_bag(request, pk):
    item = get_object_or_404(models.ProductInShoppingBag, id=pk)
    item.delete()
    return redirect('shopping')


@login_required()
def create_purchase(request):
    items_in_bag = models.ProductInShoppingBag.objects.filter(client=request.user)
    if not items_in_bag:
        return redirect('shopping')
    purchase = models.Purchase.objects.create(client=request.user, date_of_purchase=datetime.now(), total_price=0)

    price_without_sale = 0
    sale = 0
    for item in items_in_bag:
        models.ProductInPurchase.objects.create(product=item.product, purchase=purchase)
        price_without_sale += item.product.price
        if hasattr(item.product, 'sale'):
            sale += item.product.price * (100 - item.product.sale.sale_percent) // 100
    purchase.total_price = price_without_sale - sale
    purchase.save()
    items_in_bag.delete()

    return redirect('profile')


@login_required()
def profile(request):
    context = {'purchases': models.Purchase.objects.filter(client=request.user)}
    return render(request, 'profile.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        print(form.errors)
        return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


class JewelryListView(ListView):
    model = models.Jewelry
    paginate_by = 10
    template_name = 'jewelry_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JewelryListView, self).get_context_data()
        return context


class SaleListView(ListView):
    model = models.Jewelry
    paginate_by = 10
    template_name = 'jewelry_list.html'

    def get_queryset(self):
        queryset = models.Jewelry.objects.filter(sale__isnull=False)
        return queryset


class JewelryDetailView(DetailView):
    model = models.Jewelry
    template_name = 'jewelry_detail.html'


class BrandListView(ListView):
    model = models.Brand
    paginate_by = 10
    template_name = 'brand_list.html'


class BrandDetailView(DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BrandDetailView, self).get_context_data()
        context['products'] = models.Jewelry.objects.filter(brand=context['object'])
        return context


class ShoppingBagListView(LoginRequiredMixin, ListView):
    model = models.ProductInShoppingBag
    template_name = 'shopping.html'

    def get_context_data(self, **kwargs):
        context = super(ShoppingBagListView, self).get_context_data()
        sale = 0
        price_without_sale = 0
        for obj in context['object_list']:
            price_without_sale += obj.product.price
            if hasattr(obj.product, 'sale'):
                sale += obj.product.price * (100 - obj.product.sale.sale_percent) // 100
        context['price_with_sale'] = price_without_sale - sale
        context['price_without_sale'] = price_without_sale
        context['sale'] = sale
        return context

    def get_queryset(self):
        return models.ProductInShoppingBag.objects.filter(client=self.request.user)


class PurchaseDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = models.Purchase
    template_name = 'purchase_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PurchaseDetailView, self).get_context_data()
        context['products'] = models.ProductInPurchase.objects.filter(purchase=context['object'])
        return context

    def test_func(self):
        obj = get_object_or_404(self.model, id=self.kwargs.get('pk'))
        return obj.client == self.request.user
