from typing import Collection
from django.db import models
from django.db.models.base import Model, ModelState
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices, TextChoices
from django.db.models.fields import BigAutoField
from django.db.models.fields.reverse_related import ManyToManyRel
from django.db.models.manager import ManagerDescriptor
from django.db.models.query_utils import subclasses
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(default=False)
# Create your models here.

class NavbarModel(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    categories = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.name}'

class MiniNavbarModel(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'

class Settings(models.Model):
    background_image = models.ImageField(upload_to='shop_images', default='1.jpg')
    collection_name = models.CharField(max_length=100, null=True, blank=True)
    save_up = models.IntegerField(null=True, blank=True)
    collection_text = models.CharField(max_length=100, null=True, blank=True)
    page_id = models.ForeignKey('NavbarModel', null=True, blank=True, on_delete=CASCADE, related_name='settings')

    def __str__(self):
        return f'{self.collection_name}'


class RedCard(models.Model):
    image = models.ImageField(upload_to='shop_images', default='testimonial-img-1.jpg')
    text = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class FooterHeader(models.Model):
    header = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.header}'

class Footer(models.Model):
    related_header = models.ForeignKey('FooterHeader', null=True, blank=True, on_delete=CASCADE) 
    title = models.CharField(max_length=100, null=True, blank=True)
    adress = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    mail = models.EmailField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to = 'shop_images', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    category_id= models.ManyToManyField('NavbarModel')
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    sub_categories = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.name}'

# class ProductModel(models.Model):
#     navbar_id = models.ManyToManyField('NavbarModel')
#     title = models.CharField(max_length=255, null=True, blank=True)
#     price = models.CharField(max_length=255, null=True, blank=True)
#     image = models.ImageField(upload_to='shop_images', default='miles.jpg')
#     url = models.URLField(max_length=255, null=True, blank=True)

class Catalog_Products(models.Model):
    related_navbar = models.ForeignKey('NavbarModel', null=True, blank=True, on_delete=CASCADE, related_name='catalog_products')
    related_category = models.ForeignKey('Category', null=True, blank=True, on_delete=CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    del_price = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='shop_images', default='polo-shirt-1.png')
    background_image = models.ImageField(upload_to = 'shop_images', null=True, blank=True, default='fashion-header-bg-8.jpg')
    description = models.CharField(max_length=255, null=True, blank=True)
    
    class text(models.TextChoices):
        in_stock = 'In stock'
        sold_out = 'Sold Out!'

    avilability = models.TextField(choices=text.choices, null=True, blank=True)

    size_S = models.BooleanField(default=True)
    size_M = models.BooleanField(default=True) 
    size_L = models.BooleanField(default=True)
    size_XL = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

class Product_Images(models.Model):
    related_product = models.ForeignKey(Catalog_Products, null=True, blank=True, on_delete=CASCADE)
    image = models.ImageField(upload_to = 'shop_images', null=True, blank=True, default='polo-shirt-3.png')


class Banner(models.Model):
    title_1 = models.CharField(max_length=255, null=True, blank=True)
    price_1 = models.CharField(max_length=255, null=True, blank=True)
    image_1= models.ImageField(upload_to='shop_images', default='promo-banner-1.jpg')
    url_1 = models.URLField(max_length=255, null=True, blank=True)

    title_2 = models.CharField(max_length=255, null=True, blank=True)
    price_2 = models.CharField(max_length=255, null=True, blank=True)
    image_2=  models.ImageField(upload_to='shop_images', default='promo-banner-3.jpg')
    url_2 = models.URLField(max_length=255, null=True, blank=True)

    title_3 = models.CharField(max_length=255, null=True, blank=True)
    price_3 = models.CharField(max_length=255, null=True, blank=True)
    image_3=  models.ImageField(upload_to='shop_images', default='promo-banner-3.jpg')
    url_3 = models.URLField(max_length=255, null=True, blank=True)

    title_4 = models.CharField(max_length=255, null=True, blank=True)
    price_4 = models.CharField(max_length=255, null=True, blank=True)
    image_4=  models.ImageField(upload_to='shop_images', default='promo-banner-3.jpg')
    url_4 = models.URLField(max_length=255, null=True, blank=True)

    title_5 = models.CharField(max_length=255, null=True, blank=True)
    price_5 = models.CharField(max_length=255, null=True, blank=True)
    image_5=  models.ImageField(upload_to='shop_images', default='promo-banner-3.jpg')
    url_5 = models.URLField(max_length=255, null=True, blank=True)

class Latest_Blog(models.Model):
    image = models.ImageField(upload_to='shop_images', default='promo-banner-1.jpg')
    text = models.CharField(max_length=255, null=True, blank=True)

class ClientBrand(models.Model):
    image = models.ImageField(upload_to='shop_images', default='client-brand-css3.png')

class ContactModel(models.Model):
    your_name=models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField()
    subject=models.CharField(max_length=100, null=True, blank=True)
    company=models.CharField(max_length=100, null=True, blank=True)
    message=models.TextField()

class ContactDetailsModel(models.Model):
    title=models.CharField(max_length=100, null=True, blank=True)
    subtitle=models.CharField(max_length=100, null=True, blank=True)
    phone=models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField()
    address=models.CharField(max_length=100, null=True, blank=True)
    name=models.CharField(max_length=100, null=True, blank=True)
    description=models.CharField(max_length=100, null=True, blank=True)
    map=models.CharField(max_length=700, null=True, blank=True)

class ReviewModel(models.Model):
    your_review = models.CharField(max_length=100, null=True, blank=True)
    name=models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField()
