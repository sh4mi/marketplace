from django.urls import path, include
from .views import *

app_name = 'dashboard'
urlpatterns = [
    
    path('', IndexPageView.as_view(), name='index'),
    path('products/add', AddProductView, name='add_product'),
    path('products/edit/<slug>', EditProductView, name='edit_product'),
    path('products', ProductsView.as_view(), name='products'),
    path('orders', OrdersView.as_view(), name='orders'),
    path('edit/profile', EditProfileView.as_view(), name='edit_profile'),
]