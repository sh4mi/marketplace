from django.views.generic import TemplateView
from shops.models import *


class IndexPageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_list = []

        top_categories = Category.objects.filter(top_category=True)[
            :5]
        for category in top_categories:
            products = Product.objects.filter(product_categories=category)
            if products:
                for product in products:
                    print(product)
                    product_list.append(product)
        context['top_categories'] = top_categories
        print(product_list)
        context['products'] = product_list
        # context['vendor'] = vendor
        return context


class ShopPageView(TemplateView):
    template_name = 'main/shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_list = []
        categories_list = []
        top_categories = Category.objects.filter(top_category=True)[
            :5]
        for tc in top_categories:
            categories = Categories.objects.filter(category=tc)
            for category in categories:
                print(category)
                categories_list.append(category)
        for category in top_categories:
            products = Product.objects.filter(product_categories=category)
            if products:
                for product in products:
                    # print(product)
                    product_list.append(product)
        context['categories'] = categories_list
        context['products'] = product_list
        print(categories_list)
        return context


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'

class contactPageView(TemplateView):
    template_name = 'main/contact.html'

class product_detailPageView(TemplateView):
        template_name = 'main/product_detail.html'

class shop_cartPageView(TemplateView):
        template_name = 'main/shop_cart.html'

class checkoutPageView(TemplateView):
        template_name = 'main/checkout.html'


class project_managmentPageView(TemplateView):
    template_name = 'main/project_managment.html'



