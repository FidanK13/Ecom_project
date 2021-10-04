from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.query_utils import subclasses
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
    background_image = models.ImageField(upload_to = 'shop_images', null=True, blank=True)
    collection_name = models.CharField(max_length=100, null=True, blank=True)
    save_up = models.IntegerField(null=True, blank=True)
    collection_text = models.CharField(max_length=100, null=True, blank=True)
    latest_blog_images = models.ImageField(upload_to = 'shop_images', null=True, blank=True)
    latest_blog_text = models.CharField(max_length=100, null=True, blank=True)
    brand_images = models.ImageField(upload_to = 'shop_images', null=True, blank=True)
    redcard_image = models.ImageField(upload_to = 'shop_images', null=True, blank=True)
    redcard_text = models.CharField(max_length=2555, null=True, blank=True)
    redcard_name = models.CharField(max_length=2555, null=True, blank=True)
    redcard_url = models.URLField(null=True, blank=True)

#class RedCard(models.Model):
    

class Footer(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    logo = models.ImageField(upload_to = 'shop_images', null=True, blank=True)

class Category(models.Model):
    category_id= models.ManyToManyField('NavbarModel')
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    sub_categories = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.name}'

class Sub_Category(models.Model):
    subcategory_id= models.ManyToManyField('Category')
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class ProductModel1(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to = 'shop_images', null=True, blank=True)
  
class ProductModel2(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to = 'shop_images', null=True, blank=True)

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
