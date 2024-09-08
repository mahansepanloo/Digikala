

from django.db import models
from django.contrib.auth.models import User
class Seller(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    city = models.CharField(max_length = 30, verbose_name = 'city_name', help_text = 'cities name should be less than 30 characters', blank = True, null = True)
    address = models.TextField(blank=True, null=True)


    def __str__(self) -> str:
        return self.username.username

class Costumer(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, verbose_name='city_name',
                            help_text='cities name should be less than 30 characters', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    def __str__(self) -> str:
        return self.username.username