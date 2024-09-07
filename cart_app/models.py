from django.db import models
from product_app.models import Product
from accounts.models import Costumer, Seller

class Cart(models.Model):
    buyer = models.ForeignKey(Costumer, on_delete = models.CASCADE,blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    is_finalized = models.BooleanField(default=True, blank=True, null=True)
    bill = models.FloatField(blank=True, null=True)

    def total_cart(self):
        return sum(item.price * item.num for item in self.cart_item_set.all())

    

    def __str__(self) -> str:
        return f'{self.buyer}, {self.code}'
    
class Cart_item(models.Model):
    seller = models.ForeignKey(Seller, on_delete= models.CASCADE,blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete= models.CASCADE, help_text='this product', blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    num = models.IntegerField(blank= True, null=True)

    def total_cart(self):
        return self.product.price * self.num

    def __str__(self) -> str:
        return f'{self.cart}, {self.product}, {self.seller}'
