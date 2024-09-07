from django.contrib.admin import register, ModelAdmin
from accounts.models import Seller, Costumer


@register(Seller)
class Selleradmin(ModelAdmin):
    list_display = [
        'name',
        'username',
        'city'
    ]
    search_fields = [
        'name',
        'username',
        'city'
    ]

@register(Costumer)
class Costumeradmin(ModelAdmin):
    list_display = [
        'name',
        'username',
        'city'
    ]
    search_fields = [
        'name',
        'username',
        'city'
    ]
    
