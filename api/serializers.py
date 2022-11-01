from .models import Category, Product
from rest_framework import serializers


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price')

    def create(self, validated_data):
        product = Product.objects.create(title=validated_data.get('title'),
                                         price=validated_data.get('price'))
        return product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
