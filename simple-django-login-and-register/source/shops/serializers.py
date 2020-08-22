from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ('id', 'url', 'name', 'slug','top_category')
