from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("order", views.order, name="order"),
    path("ajax", views.ajax, name="ajax"),
    path("ajax2", views.ajax2, name="ajax2"),
    path("viewcart", views.viewcart, name="viewcart"),
    path("addtocart", views.addtocart, name="addtocart"),
    path("addtocart_dinner", views.addtocart_dinner, name="addtocart_dinner"),
    path("addtocart_pasta_salad", views.addtocart_pasta_salad, name="addtocart_pasta_salad"),
    path("addtocart_sub", views.addtocart_sub, name="addtocart_sub"),
    path("buy", views.buy, name = "buy"),
    path("placeorder", views.placeorder, name="placeorder"),
    path("orderhistory", views.orderhistory, name="orderhistory")
]
