from django.contrib import admin
from ecom_app.models import NavbarModel, Settings, Footer, ProductModel1,ProductModel2, Category,Sub_Category, ContactModel, ContactDetailsModel
# Register your models here.

admin.site.register(NavbarModel)
admin.site.register(Settings)
admin.site.register(Footer)
admin.site.register(ProductModel1)
admin.site.register(ProductModel2)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(ContactModel)
admin.site.register(ContactDetailsModel)