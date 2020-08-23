from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', views.CategoryView)
router.register('shop', views.ShopView)
router.register('Image', views.ImageView)
router.register('Categories', views.CategoriesView)
router.register('Product', views.ProductView)
router.register('Activation', views.ActivationView)
router.register('Address', views.AddressView)
router.register('Vendor', views.VendorView)

urlpatterns = [
    path('', include(router.urls))
]