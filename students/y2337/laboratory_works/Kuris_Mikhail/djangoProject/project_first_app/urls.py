from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items', views.get_items, name='items'),
    path('fairs', views.get_fairs, name='fairs'),
    path('results', views.get_results, name='results'),
    path('items/add_item/', views.AddItem.as_view(), name="add_item"),
    path("items/update/<int:pk>", views.UpdateItem.as_view(), name="update_item"),
    path('deleteItem/<int:id>/', views.deleteItem),
    path('results/add_results/', views.AddRes.as_view(), name="add_results"),
    path("results/update/<int:pk>", views.UpdateRes.as_view(), name="update_results"),
    path('deleteRes/<int:item_id>/', views.deleteResult),
]