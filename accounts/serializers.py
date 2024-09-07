from rest_framework import serializers
from .models import Costumer, Seller

class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = ['name', 'city', 'username', 'email', 'address', 'password']

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['name', 'city', 'username', 'email', 'address', 'password']