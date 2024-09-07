from django.db import models
from accounts.models import Costumer, Seller
from product_app.models import Product
from cart_app.models import Cart

class Discount(models.Model):
    active = models.BooleanField(default=True, blank=True, null=True)
    buyer = models.ForeignKey(Costumer, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Customer")
    code = models.CharField(max_length=10, unique=True, help_text='Code should not be more than 10 characters', blank=True, null=True, verbose_name="Discount Code")
    initiated_date = models.DateField(auto_now_add=True, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True, verbose_name="Discount Percentage")

    def __str__(self) -> str:
        return self.code

class Order(models.Model):
    buyer = models.ForeignKey(Costumer, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Customerr")
    transaction_status = models.BooleanField(blank=True, null=True)
    date = models.DateField(auto_now_add=True, help_text='The time when the order was first set', blank=True, null=True)
    discount_code = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True)
    bill = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=10, unique=True, blank=True, null=True, verbose_name="Order Code")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)

    def total_price(self):
        return sum(item.price * item.num for item in self.order_item_set.all())

    def __str__(self) -> str:
        return f'Order {self.code} by {self.buyer}'

class OrderItem(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True, null=True,verbose_name = "seller")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, help_text='This item is related to which order', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text='This product', blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True, verbose_name="Quantity")

    def __str__(self) -> str:
        return f'{self.num} x {self.product} for {self.order}'

    def total_price(self):
        return self.num * self.product.price
