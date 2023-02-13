from django.contrib import admin
from .models import Item, Order, Discount, Tax


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)


admin.site.register(Order)
