from django.db import models
from django.contrib.auth.models import User
# from shops.models import Image
import uuid
import os


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)


def get_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('', filename)


class Address(models.Model):
    address = models.CharField(max_length=150, default="", blank=True)
    city = models.CharField(max_length=150, default="", blank=True)
    state = models.CharField(max_length=150, default="", blank=True)
    country = models.CharField(max_length=150, default="", blank=True)

    def __str__(self):
        return self.address


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, default="")
    bio = models.CharField(max_length=250, default="")
    image = models.ImageField(upload_to=get_image_filename, null=True, blank=True,
                              default="vendor_placeholder.jpg", verbose_name='vendor_image')
    active = models.BooleanField(default=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Vendor: {}'.format(self.user.username)
