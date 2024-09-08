from django.urls import path
from .views import Login, Refresh, Costomer, SellerListView, FindCostumerByNameView, FindSellerByNameView

urlpatterns = [
    path('api/login/', Login.as_view(), name='login'),
    path('api/token/refresh/', Refresh.as_view(), name='token_refresh'),
    path('api/customers/', Costomer.as_view(), name='customer_list_create'),
    path('api/sellers/', SellerListView.as_view(), name='seller_list_create'),
    path('api/customers/find', FindCostumerByNameView.as_view(), name='find_customer_by_name'),
    path('api/sellers/find', FindSellerByNameView.as_view(), name='find_seller_by_name'),
]