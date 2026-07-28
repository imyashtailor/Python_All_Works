from rest_framework import serializers  
from ecom.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth=1


    def validate(self,attrs):
        if attrs['qty']<1:
            raise serializers.ValidationError({'qty':'Qty must not be 0'})
        return attrs