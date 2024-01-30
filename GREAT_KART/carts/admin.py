from django.contrib import admin

from GREAT_KART.carts.models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)

# 2nd WAY FOR REGISTER
# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ('cart_id', 'date_added')
#
#
# @admin.register(CartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ('product', 'cart', 'quantity', 'is_active')

