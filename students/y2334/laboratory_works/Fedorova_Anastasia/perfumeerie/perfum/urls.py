from django.urls import path, include
from . import views

broker = [
    path('list/', views.BrokerListView.as_view()),
    path('insert/', views.BrokerCreateView.as_view()),
    path('insert/succ/', views.BrokerListView.as_view()),
    path('<int:broker_id>', views.broker_detail),
]

buyer = [
    path('list/', views.BuyerListView.as_view()),
    path('insert/', views.BuyerCreateView.as_view()),
    path('insert/succ/', views.BuyerListView.as_view()),
    path('<int:bid>', views.buyer_detail),
]

deal = [
    path('list/', views.DealListView.as_view()),
    path('insert/', views.DealCreateView.as_view()),
    path('insert/succ/', views.DealListView.as_view()),
    path('<int:deal_id>', views.deal_detail),
]

product = [
    path('list/', views.ProductListView.as_view()),
    path('insert/', views.ProductCreateView.as_view()),
    path('insert/succ', views.ProductListView.as_view()),
    path('<int:product_id>', views.product_detail),
]

seller = [
    path('list/', views.SellerListView.as_view()),
    path('insert/', views.SellerCreateView.as_view()),
    path('insert/succ', views.SellerListView.as_view()),
    path('<int:seller_id>', views.seller_detail),
]


urlpatterns = [
    path('', views.index),
    path('broker/', include(broker)),
    path('buyer/', include(buyer)),
    path('deal/', include(deal)),
    path('product/', include(product)),
    path('seller/', include(seller)),
]
