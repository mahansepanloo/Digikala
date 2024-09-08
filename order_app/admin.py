from django.contrib.admin import register, ModelAdmin
from django.contrib import admin
from order_app.models import Order,OrderItem



class Order_itemadmin(admin.StackedInline):
    model = OrderItem

    list_display = [
        'order',
        'seller',
        'product',
        'num'
    ]
    search_fields = [
        'order',
        'seller',
        'product'
    ]


@register(Order)
class Orderadmin(ModelAdmin):
    list_display = [
        'buyer',
        'code',
        'total_price'


    ]
    search_fields = [
        'buyer',
        'code'
    ]

    inlines = (Order_itemadmin,)
