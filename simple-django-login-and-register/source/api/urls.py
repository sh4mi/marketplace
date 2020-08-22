from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', views.CategoryView)
router.register('shop', views.ShopView)


urlpatterns = [
    path('', include(router.urls))
]