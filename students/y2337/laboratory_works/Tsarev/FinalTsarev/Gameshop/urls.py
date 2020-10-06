from django.urls import path
from .views import *


urlpatterns = [
    path("", genres_list, name='genre_list_url'),
    path("games/", games_list, name='game_list_url'),
    path('games_detail/<int:game_id>/', GameDetail.as_view(), name='game_detail_url'),
    path('genre_detail/<int:genre_id>/', GenreDetail.as_view(), name='genre_detail_url'),
    path("cart/", CartView.as_view(), name='cart_url'),
    path("add_to_cart/<int:game_id>/", AddToCart.as_view(), name='add_to_cart_url'),
    path("remove_from_cart/<int:game_id>/", RemoveFromCart.as_view(), name='remove_from_cart_url'),
    path("change_qty/<int:game_id>/", ChangeQTYView.as_view(), name='change_qty_url'),
    path("checkout/", Checkout.as_view(), name='checkout_url'),
    path("make_order/", MakeOrderView.as_view(), name='make_order_url'),
]
