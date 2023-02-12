from django.contrib import admin
from .models import Item, Order

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price' )


admin.site.register(Order)

