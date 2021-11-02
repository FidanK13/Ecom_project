from django.contrib import admin
from ecom_app.models import ContactDetailsModel, ContactModel, FooterHeader, NavbarModel, Settings, Footer, ProductModel, Category, Banner, Catalog_Products, RedCard, Latest_Blog, ClientBrand
# Register your models here.

admin.site.register(NavbarModel)
admin.site.register(Settings)
admin.site.register(Footer)
admin.site.register(ProductModel)
admin.site.register(Category)

admin.site.register(Banner)
# admin.site.register(MenProduct)
# admin.site.register(WomenProduct)
# admin.site.register(SportsProduct)
# admin.site.register(ElectronicsProduct)
admin.site.register(RedCard)
admin.site.register(Latest_Blog)
admin.site.register(ClientBrand)
admin.site.register(ContactModel)
admin.site.register(ContactDetailsModel)
admin.site.register(Catalog_Products)
admin.site.register(FooterHeader)
