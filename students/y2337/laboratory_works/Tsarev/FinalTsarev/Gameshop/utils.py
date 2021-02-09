from django.db import models


def recalc_cart(cart):
    cart_data = cart.games.aggregate(models.Sum("final_price"), models.Count("id"), models.Sum("qty"))
    if cart_data.get("final_price__sum"):
        cart.final_price = cart_data["final_price__sum"]
    else:
        cart.final_price = 0
    if not cart_data["qty__sum"]:
        cart.total_games = cart_data["id__count"]
    else:
        cart.total_games = cart_data["qty__sum"]
    cart.save()