from django.urls import path 
from .views import  account_view, category_view, contact_view, filtired_product_view, home_view, logout_view, product_detail_view, product_view

urlpatterns = [
    path('', home_view, name = 'home_page'),
    path('contact/', contact_view, name='contact_page'),
    path('category/<int:navbar_id>/', category_view, name='category_page'),
    path('product_detail/<int:product_id>/', product_detail_view, name='product_detail_page'),
    path('product/<int:name>/', product_view, name="product_page"),
    path('product/<int:name>/<int:catalog_id>/', filtired_product_view, name="filtired_product_page"),
    path('account/', account_view, name='account_page'),
    path('logout/', logout_view, name='logout_page')
]