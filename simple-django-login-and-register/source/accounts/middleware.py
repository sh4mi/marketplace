

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from shops.models import Vendor


class CheckVendorMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # print(request.user)
        if request.user.is_authenticated:
            user = request.user
            check_vendor = Vendor.objects.filter(user=user)
            if check_vendor:
                vendor = True
            else:
                vendor = False
            print(vendor)

        return None
