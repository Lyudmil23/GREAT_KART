from django.urls import path

from GREAT_KART.carts.views import cart, add_cart

urlpatterns = [
    path('', cart, name='cart'),
    path('add_cart/<int:product_id>/', add_cart, name='add_cart'),
]