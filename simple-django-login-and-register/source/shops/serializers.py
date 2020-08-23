from rest_framework import serializers
from .models import Category, Shop, Image, Categories, Product


class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ('id', 'url', 'name', 'slug','top_category')


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'url', 'name', 'slug', 'vendor','address','phone','phone2')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'url', 'image', 'created_at')

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'url', 'category', 'children')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'url', 'shop', 'name', 'slug', 'short_description', 'long_description', 'product_categories', 'images', 'price', 'discounted_price', 'quantity', 'created_at', 'updated_at')


