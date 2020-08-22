from django.shortcuts import render
from rest_framework import viewsets
from shops.models import Category,Shop
from shops.serializers import CategorySerializer,ShopSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ShopView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer