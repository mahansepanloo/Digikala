from django.contrib.admin import ModelAdmin, register
from product_app.models import Product, Category, Comment, Rate

@register(Product)
class Productadmin(ModelAdmin):
    list_display = [
        'name',
        'price',
        'stock'
    ]
    search_fields = [
        'name'
    ]

@register(Category)
class Categoryadmin(ModelAdmin):
    list_display = [
        'name',
    ]
    search_fields = [
        'name'
    ]

@register(Comment)
class Commentadmin(ModelAdmin):
    list_display = [
        'comment_text',
        'buyer'
    ]
    search_fields = [
        'buyer'
    ]

@register(Rate)
class Rateadmin(ModelAdmin):
    list_display = [
        'rating',
        'rater'
    ]
    search_fields = [
        'rater'
    ]
