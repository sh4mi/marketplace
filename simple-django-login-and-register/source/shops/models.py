from django.db import models
from django.contrib.auth.models import User
from accounts.models import Vendor
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
import uuid
import os
from django.utils.text import slugify


class Shop(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(unique=True,blank=True)
    phone = models.CharField(max_length=20, default="")
    phone2 = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Shop, self).save(*args, **kwargs)

    def __str__(self):
        return 'Shop: {}'.format(self.name)


def get_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('', filename)


class Image(models.Model):
    image = models.ImageField(upload_to=get_image_filename, null=True, blank=True, default="product_placeholder.jpg",
                              verbose_name='product_image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    top_category = models.BooleanField(default=False)
    slug = models.SlugField(unique=True,blank=True)
    # unique name constraint in name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Categories(models.Model):
    category = models.OneToOneField(
        Category, on_delete=models.CASCADE, related_name='category_obj')
    children = models.ManyToManyField(Category)

    def __str__(self):
        return self.category.name
    # this function is linked with category. so that when any category is created we can store its children inside it.
    # when new category created this function will called and create a empty relation ship with category model with zero children. but we can add multple childrens later.

    def create_category(sender, **kwargs):
        category = kwargs["instance"]
        if kwargs["created"]:
            category_profile = Categories(category=category)
            category_profile.save()
    post_save.connect(create_category, sender=Category)


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    slug = models.SlugField(unique=True,blank=True)
    short_description = models.CharField(
        max_length=250, blank=True, default='')
    long_description = models.TextField(blank=True, default='')
    product_categories = models.ManyToManyField(Category,blank=True)
    images = models.ManyToManyField(Image, related_name="product_image",blank=True)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    quantity = models.IntegerField(blank=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
