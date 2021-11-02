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


class RedCard(models.Model):
    image = models.ImageField(upload_to = 'shop_images', null=True, blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

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

# class SubCategory(models.Model):
#     subcategory_id = models.ManyToManyField('Category')
#     name = models.CharField(max_length=255, null=True, blank=True)
#     url = models.URLField(max_length=255, null=True, blank=True)

class ProductModel(models.Model):
    navbar_id = models.ManyToManyField('NavbarModel')
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='shop_images', null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)

class Banner(models.Model):
    title_1 = models.CharField(max_length=255, null=True, blank=True)
    price_1 = models.CharField(max_length=255, null=True, blank=True)
    image_1= models.ImageField(upload_to = 'shop_images', null=True, blank=True)

    title_2 = models.CharField(max_length=255, null=True, blank=True)
    price_2 = models.CharField(max_length=255, null=True, blank=True)
    image_2= models.ImageField(upload_to = 'shop_images', null=True, blank=True)

    title_3 = models.CharField(max_length=255, null=True, blank=True)
    price_3 = models.CharField(max_length=255, null=True, blank=True)
    image_3= models.ImageField(upload_to = 'shop_images', null=True, blank=True)

    title_4 = models.CharField(max_length=255, null=True, blank=True)
    price_4 = models.CharField(max_length=255, null=True, blank=True)
    image_4= models.ImageField(upload_to = 'shop_images', null=True, blank=True)

    title_5 = models.CharField(max_length=255, null=True, blank=True)
    price_5 = models.CharField(max_length=255, null=True, blank=True)
    image_5= models.ImageField(upload_to = 'shop_images', null=True, blank=True)

class MenProduct(models.Model):
    name_product = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True) 
    image = models.ImageField(upload_to = 'shop_images', null=True, blank=True)

class WomenProduct(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to = 'shop_images', null=True, blank=True)

class SportsProduct(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to = 'shop_images', null=True, blank=True)

class ElectronicsProduct(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to = 'shop_images', null=True, blank=True)

class Latest_Blog(models.Model):
    image = models.ImageField(upload_to = 'shop_images', null=True, blank=True)
    text = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True,blank=True)

class ClientBrand(models.Model):
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
