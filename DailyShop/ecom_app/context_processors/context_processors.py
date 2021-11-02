from ecom_app.models import Footer, NavbarModel, Settings

def context(request):
    context = {}
    
    navbar_queryset = NavbarModel.objects.all()
    settings_queryset = Settings.objects.all()
    footer_queryset = Footer.objects.all()

    context['footer_queryset'] = footer_queryset
    context['navbar_queryset'] = navbar_queryset
    context['settings_queryset'] = settings_queryset

    return context