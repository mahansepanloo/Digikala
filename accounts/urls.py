from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login', Login),
    path('Refresh', Refresh),

    path('costumers', costumers_list_func),
    path('sellers', sellers_list_func),
    path('costumers/<str:input_name>', find_costumers_by_name),
    path('sellers/<str:input_name>', find_sellers_by_name),
    path('costumers/find_costumers_by_username/<str:input_username>', find_costumers_by_username),
    path('sellers/find_sellers_by_username/<str:input_username>', find_sellers_by_username),
    path('add_seller', add_seller),
    path('add_costumer', add_costumer),]