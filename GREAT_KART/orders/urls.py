from django.urls import path

from GREAT_KART.orders.views import place_order, payments, order_complete

urlpatterns = [
    path('place_order/', place_order, name='place_order'),
    path('payments/', payments, name='payments'),
    path('order_complete/', order_complete, name='order_complete'),

]