from django.urls import path
from cart_app.views import *

urlpatterns = [
    path('carts_list', cart_list_func),
    path('cart_items_list', cart_item_func),
    path('carts_list/by_seller/<str:seller_name>',cart_item_by_seller),
    path('carts_list/by_buyer/<str:buyer_name>',cart_by_buyer),
    path('cart_item_by_product/<product_name>', cart_item_by_product),
    path('cart_by_code/<code_input>', cart_by_code),
    path('add_cart', add_cart),
    path('add_cart_item', add_cart_item),]