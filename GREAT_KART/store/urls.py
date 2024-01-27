from django.urls import path

from GREAT_KART.store.views import store

urlpatterns = [
    path('', store, name='store'),
    path('<slug:category_slug>/', store, name='products_by_category'),

]