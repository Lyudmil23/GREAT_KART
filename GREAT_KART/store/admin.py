from django.contrib import admin
from GREAT_KART.store.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Product, ProductAdmin)


##2nd way for register
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
#     prepopulated_fields = {'slug': ('product_name',)}


