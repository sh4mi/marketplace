from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from main.views import IndexPageView, ChangeLanguageView, ShopPageView, contactPageView, product_detailPageView, shop_cartPageView, checkoutPageView, project_managmentPageView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView.as_view(), name='index'),
    path('shop/', ShopPageView.as_view(), name='shop'),
    path('contact/', contactPageView.as_view(), name='contact'),
    path('checkout/', checkoutPageView.as_view(), name='checkout'),
    path('project_managment/', project_managmentPageView.as_view(), name='project_managment'),
    path('shop_cart/', shop_cartPageView.as_view(), name='shop_cart'),
    # path('About/', AboutPageView.as_view(), name='About'),
    path('product_detail/', product_detailPageView.as_view(), name='product_detail'),
    # path('product/<name>')
    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('api/', include('api.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
