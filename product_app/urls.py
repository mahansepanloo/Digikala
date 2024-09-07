from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    CategoryListCreateView, CategoryDetailView,
    CommentListCreateView, CommentDetailView,
    RateListCreateView, RateDetailView
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),

    path('rates/', RateListCreateView.as_view(), name='rate-list-create'),
    path('rates/<int:pk>/', RateDetailView.as_view(), name='rate-detail'),
]