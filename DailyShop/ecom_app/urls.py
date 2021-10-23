from django.urls import path 
from .views import home_view, contact_view,catalog_view, category_view,product_view, account_view

urlpatterns = [
    path('', home_view, name = 'home_page'),
    path('contact/', contact_view),
    path('catalog/', catalog_view),
    path('category/<int:navbar_id>/', category_view, name='category_page'),
    path('product/', product_view, name='product_page'),
    path('account/', account_view, name='account_page'),
]