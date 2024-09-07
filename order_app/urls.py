from django.urls import path
from .views import (
    DiscountListCreateView, DiscountDetailView,
    OrderListCreateView, OrderDetailView,
    OrderItemListCreateView, OrderItemDetailView
)

urlpatterns = [
    path('discounts/', DiscountListCreateView.as_view(), name='discount-list-create'),
    path('discounts/<int:pk>/', DiscountDetailView.as_view(), name='discount-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order-items/', OrderItemListCreateView.as_view(), name='orderitem-list-create'),
    path('order-items/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem-detail'),
]