from django.urls import path

from GREAT_KART.orders.views import place_order

urlpatterns = [
    path('place_order/', place_order, name='place_order')

]