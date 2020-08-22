from rest_framework import serializers
from .models import Category, Shop

class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ('id', 'url', 'name', 'slug','top_category')


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'url', 'name', 'slug', 'vendor','address','phone','phone2')