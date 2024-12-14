from django.contrib import admin
from .models import Supplier, Ingredient, MenuItem, Order

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'contact_info')

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient_name', 'stock_quantity', 'unit', 'expiry_date')

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('menu_item_name', 'price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'quantity', 'order_date')

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)
