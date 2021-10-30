from ecom_app.models import NavbarModel, Settings, Footer, CategoryModel

def context(request):
    context={}
    navbar_queryset = NavbarModel.objects.all()
    settings_queryset = Settings.objects.all().first()
    footer_queryset = Footer.objects.all()
    # mininavbar_queryset = MiniNavbarModel.objects.all()
    # redcard_queryset = RedCard.objects.all()
    #product_queryset = ProductModel.objects.all()
    category_queryset = CategoryModel.objects.all()
    #subcategory_queryset = SubCategoryModel.objects.all()

    context['navbar_queryset'] = navbar_queryset
    context['settings_queryset'] = settings_queryset
    context['footer_queryset'] = footer_queryset
    #context['product'] = product_queryset
    context['category_queryset'] = category_queryset
    #context['subcategory_queryset'] = subcategory_queryset


    return context #render(request, 'index.html', context)