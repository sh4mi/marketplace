from django.shortcuts import render
from django.views.generic import TemplateView
from shops.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, FormView, TemplateView

from .forms import * 

class IndexPageView(TemplateView):
    template_name = 'dashboard/index.html'

# class AddProductView(TemplateView):
    # template_name = 'dashboard/add_product.html'

class EditProfileView(TemplateView):
    template_name = 'dashboard/edit_profile.html'

class ProductsView(TemplateView):
    template_name = 'dashboard/products.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        check_vendor = Vendor.objects.get(user=user)
        if check_vendor:
            print("yes he is a vendor go ahead")
            shop = Shop.objects.get(vendor=check_vendor)
            products = Product.objects.filter(shop=shop)
        context['products'] = products
        return context

class OrdersView(TemplateView):
    template_name = 'dashboard/orders.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        check_vendor = Vendor.objects.get(user=user)
        if check_vendor:
            print("yes he is a vendor go ahead")
            shop = Shop.objects.get(vendor=check_vendor)
            products = Product.objects.filter(shop=shop)
        context['products'] = products
        return context

def AddProductView(request):
    errors=[]
    categories = Category.objects.all()
    if request.method == 'POST':
        user = request.user
        check_vendor = Vendor.objects.get(user=user)
        if check_vendor:
            print("yes he is a vendor go ahead")
            shop = Shop.objects.get(vendor=check_vendor)
            req = request.POST
            
            name = req['name']
            product = Product()
            product.name = req['name']
            product.price = req['price']
            product.discounted_price = req['discounted_price']
            product.short_description=req['short_description']
            product.shop= shop
            categories = req.getlist('categories')
            product.save()
            for category in categories:
                category = Category.objects.get(slug=category)
                product.product_categories.add(category)
                product.save()
                print(category)
            
        else:
            errors.append("you are not registered as vendor")
    else:
        print("get")
        
    return render(request, 'dashboard/add_product.html', {'errors': errors,'categories':categories})



def EditProductView(request,slug):
    errors=[]
    categories = Category.objects.all()
    if request.method == 'POST':
        user = request.user
        check_vendor = Vendor.objects.get(user=user)
        if check_vendor:
            print("yes he is a vendor go ahead")
            shop = Shop.objects.get(vendor=check_vendor)
            req = request.POST
            
            name = req['name']
            product = Product()
            product.name = req['name']
            product.price = req['price']
            product.discounted_price = req['discounted_price']
            product.short_description=req['short_description']
            product.shop= shop
            categories = req.getlist('categories')
            product.save()
            for category in categories:
                category = Category.objects.get(slug=category)
                product.product_categories.add(category)
                product.save()
                print(category)
            
        else:
            errors.append("you are not registered as vendor")
    else:
        print(slug)
        
    return render(request, 'dashboard/edit_product.html', {'errors': errors,'categories':categories})
