from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'seller_name', help_text = 'seller name should be less than 50 characters',blank = True, null = True)
    city = models.CharField(max_length = 30, verbose_name = 'city_name', help_text = 'cities name should be less than 30 characters', blank = True, null = True)
    username = models.CharField(max_length = 36, help_text = 'username should be less than 36 characters',blank = True, null = True)
    password = models.CharField(max_length= 36, help_text = 'password should be less than 50 characters',blank = True, null = True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    
    def __str__(self) -> str:
        return self.name

class Costumer(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'costumer_name', help_text = 'costumer name should be less than 50 characters', blank = True, null = True)
    city = models.CharField(max_length = 30, verbose_name = 'city_name', help_text = 'cities name should be less than 30 characters', blank=True, null=True)
    username = models.CharField(max_length = 36, help_text = 'username should be less than 36 characters',blank = True, null = True)
    password = models.CharField(max_length= 36, help_text = 'password should be less than 50 characters',blank = True, null = True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)


    def __str__(self) -> str:
        return self.name
