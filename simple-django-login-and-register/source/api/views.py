from django.shortcuts import render
from rest_framework import viewsets
from shops.models import Category,Shop,Image,Categories,Product
from shops.serializers import CategorySerializer,ShopSerializer,ImageSerializer,CategoriesSerializer,ProductSerializer
from accounts.models import Activation,Address,Vendor
from accounts.serializers import ActivationSerializer,AddressSerializer,VendorSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ShopView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class CategoriesView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ActivationView(viewsets.ModelViewSet):
    queryset = Activation.objects.all()
    serializer_class = ActivationSerializer

class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class VendorView(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer