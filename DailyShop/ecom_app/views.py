from django.contrib.admin.sites import site
from django.db.models.deletion import RESTRICT
from django.shortcuts import render
from django.template.response import ContentNotRenderedError
from .models import NavbarModel, Settings, Footer, MiniNavbarModel, Category, Sub_Category, ProductModel1, ProductModel2

def home_view(request):
    context = {}
    navbar_queryset = NavbarModel.objects.all()
    settings_queryset =  Settings.objects.all().first()
    footer_queryset = Footer.objects.all()
    # mininavbar_queryset = MiniNavbarModel.objects.all()
    # redcard_queryset = RedCard.objects.all()
    product1_queryset = ProductModel1.objects.all()
    product2_queryset = ProductModel2.objects.all()
    category_queryset = Category.objects.all()
    subcategory_queryset =Sub_Category.objects.all()

    context['navbar_queryset'] = navbar_queryset
    context['settings_queryset'] = settings_queryset
    context['footer_queryset'] = footer_queryset
    context['product1'] = product1_queryset
    context['product2'] = product2_queryset
    context['category_queryset'] = category_queryset
    context['subcategory_queryset'] = subcategory_queryset

    return render(request, 'index.html', context)