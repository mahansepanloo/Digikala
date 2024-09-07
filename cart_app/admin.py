from django.contrib.admin import register, ModelAdmin
from django.contrib import admin
from cart_app.models import Cart, Cart_item





class Cart_timeadmin(admin.StackedInline):
    model = Cart_item
    list_display = [
        'cart',
        'seller',
        'product',
        'num'
    ]
    search_fields = [
        'cart',
        'seller',
        'product'
    ]
@register(Cart)
class CartAdmin(ModelAdmin):
    list_display = [
        'buyer',
        'code',
        'total_cart'
    ]
    search_fields = [
        'buyer',
    ]

    inlines = (Cart_timeadmin,)
