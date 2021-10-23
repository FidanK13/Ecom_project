from django.contrib.admin.sites import site
from django.db.models.deletion import RESTRICT
from django.shortcuts import render , redirect
from django.template.response import ContentNotRenderedError
from .models import NavbarModel, Settings, Footer, CategoryModel,\
     ContactModel, ContactDetailsModel , \
    ClientBrand, MenProduct,  Banner, WomenProduct,\
     SportsProduct,ElectronicsProduct,\
     RedCard, Latest_Blog, ProductModel
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def home_view(request):
    context = {}
    #navbar_queryset = NavbarModel.objects.all()
    #settings_queryset = Settings.objects.all().first()
    #footer_queryset = Footer.objects.all()
    # mininavbar_queryset = MiniNavbarModel.objects.all()
    # redcard_queryset = RedCard.objects.all()
    product_queryset = ProductModel.objects.all()
    #category_queryset = CategoryModel.objects.all()
    #subcategory_queryset = SubCategoryModel.objects.all()
    redcard_queryset = RedCard.objects.all()
    #product_queryset = ProductModel.objects.all()
    # category_queryset = Category.objects.all()
    banner_queryset = Banner.objects.all().first
    men_product_queryset = MenProduct.objects.all()
    women_product_queryset = WomenProduct.objects.all()
    sports_product_queryset = SportsProduct.objects.all()
    electronics_product_queryset = ElectronicsProduct.objects.all()
    latest_blog_queryset = Latest_Blog.objects.all()
    client_queryset = ClientBrand.objects.all()
    #context['navbar_queryset'] = navbar_queryset
    #context['settings_queryset'] = settings_queryset
    #context['footer_queryset'] = footer_queryset
    context['product'] = product_queryset
    #context['category_queryset'] = category_queryset
    #context['subcategory_queryset'] = subcategory_queryset
    context['product_queryset'] = product_queryset
    context['redcard'] = redcard_queryset
    # context['category_queryset'] = category_queryset
    context['banner_queryset'] = banner_queryset
    context['men_product_queryset'] = men_product_queryset
    context['women_product_queryset'] = women_product_queryset
    context['sports_product_queryset'] = sports_product_queryset
    context['electronics_product_queryset'] = electronics_product_queryset
    context['latest_blog_queryset'] =latest_blog_queryset
    context['client_queryset'] = client_queryset
    return render(request, 'index.html', context)

def contact_view(request):
    context={}
    details_queryset=ContactDetailsModel.objects.all().first()
    context['details_queryset']=details_queryset
    if request.method=='POST':
        your_name=request.POST.get("your_name",None)
        email=request.POST.get("email",None)
        subject=request.POST.get("subject",None)
        company=request.POST.get("company",None)
        message=request.POST.get("message",None)
        ContactModel.objects.create(
            your_name=your_name,
            email=email,
            subject=subject,
            company=company,
            message=message
        )
    else:
        return render(request, 'contact.html',context)

    return render(request,'contact.html', context)

def catalog_view(request):
    return render(request, 'catalog.html')


def category_view(request, navbar_id):
    context = {}
    product_queryset = ProductModel.objects.filter(navbar_id=navbar_id)
    category_queryset = CategoryModel.objects.filter(navbar_id=navbar_id)
    context['category_queryset'] = category_queryset
    context['product_queryset'] = product_queryset

    return render(request, 'category.html', context)

def product_view(request):
    return render(request, 'product.html')

def account_view(request):

    context={}
    username=request.POST.get('username')
    raw_password=request.POST.get('password')
    user=authenticate(username=username,password=raw_password)
    if user:
        login(request,user)
        return redirect('home_page')

    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home_page')

            else:
                # form=UserCreationForm()
                context['form'] = form
                # messages.error(request,form.errors)
                return render(request, 'account.html', context)
        else:
            form = UserCreationForm()
            context['form'] = form
            return render(request, 'account.html', context)
        #context['error_message']='No such user'
        #messages.error(request, "username or password is incorrect" )
        return render(request,'account.html', context)

    return render(request, 'account.html', context)
