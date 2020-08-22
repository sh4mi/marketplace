from django.shortcuts import render
from rest_framework import viewsets
from shops.models import Category
from shops.serializers import CategorySerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
