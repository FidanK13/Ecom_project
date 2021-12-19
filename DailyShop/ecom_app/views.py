from typing import Container, ContextManager
from django.contrib.admin.sites import site
from django.db.models.deletion import RESTRICT
from django.shortcuts import render, redirect
from .models import Catalog_Products, ClientBrand, ContactDetailsModel, ContactModel, FooterHeader,\
 NavbarModel, Product_Images, ReviewModel, Settings, Footer,\
 MiniNavbarModel, Category,\
 Banner, \
 RedCard, Latest_Blog, ProfileModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import LoginForm, RegisterForm, ProfileForm


def home_view(request):
    context = {}
    # navbar_queryset = NavbarModel.objects.all()
    # settings_queryset =  Settings.objects.all()
    # footer_queryset = Footer.objects.all()
    # mininavbar_queryset = MiniNavbarModel.objects.all()
    redcard_queryset = RedCard.objects.all()
    # product_queryset = ProductModel.objects.all()
    # category_queryset = Category.objects.filter(category_id=navbar_id)
    banner_queryset = Banner.objects.all().first
    # men_product_queryset = MenProduct.objects.all()
    # women_product_queryset = WomenProduct.objects.all()
    # sports_product_queryset = SportsProduct.objects.all()
    # electronics_product_queryset = ElectronicsProduct.objects.all()
    latest_blog_queryset = Latest_Blog.objects.all()
    client_queryset = ClientBrand.objects.all() 
    catalog_product = Catalog_Products.objects.all()
    
    context['catalog_product'] = catalog_product
    # context['navbar_queryset'] = navbar_queryset
    # context['settings_queryset'] = settings_queryset
    # context['footer_queryset'] = footer_queryset
    # context['product_queryset'] = product_queryset
    context['redcard'] = redcard_queryset
    # context['category_queryset'] = category_queryset
    context['banner_queryset'] = banner_queryset
    # context['men_product_queryset'] = men_product_queryset
    # context['women_product_queryset'] = women_product_queryset
    # context['sports_product_queryset'] = sports_product_queryset
    # context['electronics_product_queryset'] = electronics_product_queryset
    context['latest_blog_queryset'] =latest_blog_queryset
    context['client_queryset'] = client_queryset
    # context['subcategory_queryset'] = subcategory_queryset
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

def category_view(request, navbar_id):
    context={}
    navbar = NavbarModel.objects.all()
    # product_queryset = ProductModel.objects.filter(navbar_id=navbar_id)
    category_queryset=Category.objects.filter(category_id=navbar_id)
    context['category_queryset'] = category_queryset
    context['navbar'] = navbar
    # context['product_queryset'] = product_queryset
    return render(request, 'category.html', context)

def base_view(request):
    context = {}
    navbar_queryset = NavbarModel.objects.all()
    settings_queryset =  Settings.objects.all()
    footer_queryset = Footer.objects.all()
    # mininavbar_queryset = MiniNavbarModel.objects.all()
    redcard_queryset = RedCard.objects.all()
    # product_queryset = ProductModel.objects.all()
    # category_queryset = Category.objects.all()
    banner_queryset = Banner.objects.all().first
    # men_product_queryset = MenProduct.objects.all()
    # women_product_queryset = WomenProduct.objects.all()
    # sports_product_queryset = SportsProduct.objects.all()
    # electronics_product_queryset = ElectronicsProduct.objects.all()
    latest_blog_queryset = Latest_Blog.objects.all()
    client_queryset = ClientBrand.objects.all() 
    footer_header = FooterHeader.objects.all()
    category = Category.objects.all()
  
    context['category'] = category
    context['navbar_queryset'] = navbar_queryset
    context['settings_queryset'] = settings_queryset
    context['footer_queryset'] = footer_queryset
    # context['product_queryset'] = product_queryset
    context['redcard'] = redcard_queryset
    # context['category_queryset'] = category_queryset
    context['banner_queryset'] = banner_queryset
    # context['men_product_queryset'] = men_product_queryset
    # context['women_product_queryset'] = women_product_queryset
    # context['sports_product_queryset'] = sports_product_queryset
    # context['electronics_product_queryset'] = electronics_product_queryset
    context['latest_blog_queryset'] =latest_blog_queryset
    context['client_queryset'] = client_queryset
    # context['subcategory_queryset'] = subcategory_queryset
    context['footer_header'] = footer_header

    return render(request, 'base.html', context)

def product_detail_view(request, product_id, related_product):
    context = {}
    
    image_queryset = Product_Images.objects.filter(related_product=related_product)
    navbar_queryset = NavbarModel.objects.all()
    context['navbar_queryset'] = navbar_queryset
    # product_queryset=ProductModel.objects.filter(id=product_id)
    # context['product_queryset']= product_queryset
    catalog_product = Catalog_Products.objects.filter(id=product_id)
    context['catalog_product'] = catalog_product
    context['image_queryset'] = image_queryset

    if request.method=='POST':
        name=request.POST.get("name",None)
        email=request.POST.get("email",None)
        your_review=request.POST.get("your_review",None)
        ReviewModel.objects.create(
            name=name,
            email=email,
            your_review=your_review
        )
    else:
        return render(request, 'product-detail.html',context)

    return render(request, 'product-detail.html', context)

def product_view(request, name):
    context = {}
    
    settings = Settings.objects.filter(page_id=name)
    navbar_queryset = NavbarModel.objects.all()
    context['navbar_queryset'] = navbar_queryset
    catalog_product = Catalog_Products.objects.filter(related_navbar=name)
    context['catalog_product'] = catalog_product
    context['settings'] = settings
    return render(request, 'product.html', context)

def filtired_product_view(request, name, catalog_id):
    context = {}

    settings = Settings.objects.filter(page_id=name)
    navbar_queryset = NavbarModel.objects.all()
    context['navbar_queryset'] = navbar_queryset
    catalog_product = Catalog_Products.objects.filter(related_category=catalog_id, related_navbar=name)
    context['settings'] = settings
    context['catalog_product'] = catalog_product
    return render(request, 'product.html', context)
'''
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
'''
def logout_view(request):
    auth.logout(request)
    return redirect('home_page')

class login_view(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    #success_url = reverse_lazy('home_page')


class register_view(generic.CreateView):
    form_class = RegisterForm  #.fields['is_activated'].initial = False  #.cleaned_data(is_activated=False)   #changed_data.__setattr__(self,'is_activated',False)
    template_name = 'register.html'
    success_url = reverse_lazy('login_page')


class account_view(auth_views.LoginView): #, generic.CreateView), auth_views.LoginView)  FormView
    template_name = 'account.html'
    #def get_initial(self, request, *args, **kwargs):
    #form1 = LoginForm  # {'login': LoginForm, 'register': RegisterForm}
    #form2 = RegisterForm  # {'login': LoginForm, 'register': RegisterForm}
    def post(self, request):
        #instantiate all unique forms (using prefix) as unbound
        LoginForm    = LoginForm(prefix='LoginForm')
        RegisterForm = RegisterForm(prefix='RegisterForm')

        # determine which form is submitting (based on hidden input called 'action')
        action = self.request.POST['action']

        # bind to POST and process the correct form
        if (action == 'login'):
            LoginForm = LoginForm(request.POST, prefix='LoginForm')
            if LoginForm.is_valid():
                # user form validated, code away..
                success_url = reverse_lazy('home_page')

        elif (action == 'register'):
            RegisterForm = RegisterForm(request.POST, prefix='RegisterForm')
            if RegisterForm.is_valid():
                # billing form validated, code away..
                success_url = reverse_lazy('home_page')

        # prep context
        context = {
            'LoginForm':    LoginForm,
            'RegisterForm': RegisterForm,
        }
        return render(request, 'accounts/account.html', context)

def profile_view(request, user):
    context = {}
    profile_queryset = ProfileModel.objects.filter(user=user)
    '''
    form=ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'profile.html', context)
        else:
                    # form=UserCreationForm()
            context['form'] = form
                    # messages.error(request,form.errors)
            return render(request, 'profile.html', context)



    context['form'] = form
    '''
    context['profile_queryset'] = profile_queryset

    return render(request,'profile.html',context)


def profile_update_view(request, user):
    context={}
    profile_queryset = ProfileModel.objects.filter(user=user).first()
    update_data =ProfileModel.objects.filter(user=user).first()
    form=ProfileForm(instance=update_data )
    if request.method=='POST':
        #image=request.FILES.get('image')  #.getlist('images_all')
        form=ProfileForm(request.POST, request.FILES,instance=update_data) # , request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            '''
            ProfileModel.objects.update_or_create(
                user=form.user,
                image=image
            )
            '''
            #context['form'] = form
            #return render(request,'profile.html',context)

            return redirect('home_page')

        '''
            for i in images:
                WorkImageModel.objects.update_or_create(
                    work_id_id = form.id,
                    images=i
                )
            
            return redirect('profile_page')

        else:
            context['form']=form
            #messages.error(request,form.errors)
            return render(request,'profile_update.html',context)
        '''
    context['profile_queryset'] = profile_queryset

    context['form'] = form
    return render(request, 'profile_update.html', context)

