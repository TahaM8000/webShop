from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from stuff.models import Product,Category
from .models import ConfigShop, shop, banner, Survey, FAQGroup
from stuff.models import Brand
from blog.models import Article
from cart.cart import Cart
from accounts.views import color_messages
from accounts.forms import UserLoginForm,UserCreationForm, UserChangeForm, AddressForm
#------------------------------------------------------------------------------------------------
messages_dict = {
    "send_success" : "سوالت رو با موفقیت ارسال شد.",
    "problem_in_send" : 'مشکلی تو ارسال سوالت پیش اومد.',
}
#----------------------------------------------------------------------------------------------
def InformationsForTemplate(request):
    Info = {}
    # Categories
    allCategories = Category.objects.filter(is_sub=False)[:10]
    #wishlist
    wishlistAmount = 0
    if(request.user.is_authenticated):
        wishlistAmount = request.user.wishlist.all().count()
    #forms
    form = UserLoginForm
    #cart
    cart = Cart(request)
    CartAmount = cart.get_count()
    #forms
    Loginform = UserLoginForm
    Registerform= UserCreationForm

    #brands
    brands = Brand.objects.all()

    #shops
    shops = shop.objects.all()

    site = ConfigShop.objects.get(current=True)


    Info = {'allCategories': allCategories,'wishlistAmount':wishlistAmount,'cart':cart,'form':form
    ,'Loginform':Loginform,'Registerform':Registerform,"brands":brands,"shops":shops,'site':site}
    Info["banners"] = banner.filter()
    Info["footer_articles"] = Article.objects.all()[::-1][0:3]

    return Info
#----------------------------------------------------------------------------------------------
from .models import home_page_choices
def HomePage(request):
    # discounted stuff
    discounted = Product.objects.filter(available=True,discounted=True)[::-1][0:6]
    # New stuff in website
    news = Product.objects.filter(available=True)
    news_list = [s.id for s in news if s.is_new][0:8]
    news = news.filter(id__in=news_list)
    
    
    Info = InformationsForTemplate(request)
    Info["productsOfDiscount"] = discounted
    Info["products"] = news
    Info["articles"] = Article.objects.filter(is_for_landing=True)[0:3]
    if request.user.is_authenticated:
        Info["watched"] = request.user.wacthed.all().order_by('timestamp')[::-1][0:4]
    
    Info["categories"] = Category.objects.all()


    return render(request,f"facades/{dict(home_page_choices)[Info['site'].home_page]}.html",Info)
#----------------------------------------------------------------------------------------------
def contact(request):
    Info = InformationsForTemplate(request)

    return render(request,'facades/contact.html',Info)
#----------------------------------------------------------------------------------------------
def aboutUs(request):  
    Info = InformationsForTemplate(request)

    return render(request,'facades/aboutUs.html',Info)
#----------------------------------------------------------------------------------------------
from .models import Rule
def rules(request):  
    Info = InformationsForTemplate(request)
    rules = Rule.objects.all()
    Info['rules'] = rules
    return render(request,'facades/rules.html',Info)
#----------------------------------------------------------------------------------------------
def FAQ(request):
    FAQG = FAQGroup.objects.all()
    Info = InformationsForTemplate(request)
    Info["FAQG"] = FAQG

    return render(request,'facades/FAQ.html',Info)
#----------------------------------------------------------------------------------------------
from django.core.mail import send_mail
from .forms import SurveyForm

def CreateSurvey(request):
    CreateSurvey = False
    form = SurveyForm()
    Info = InformationsForTemplate(request)
    Info.update({'form': form,'CreateSurvey':CreateSurvey})

    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            
            text = form.cleaned_data['text']
            title = form.cleaned_data['title']

            surveyUser = Survey(
                name = name,
                email = email,
                phoneNumber = phone_number,
                title = title,
                text = text)
            surveyUser.save()

            CreateSurvey = True
            Info.update({'CreateSurvey':CreateSurvey})
            messages.success(request,messages_dict['send_success'],color_messages['success'])
            return render(request, 'facades/contact.html', Info)
        else:
            messages.error(request,messages_dict['problem_in_send'],color_messages['error'])
            return render(request, 'facades/contact.html', Info)

    return contact(request)
#----------------------------------------------------------------------------------------------
def handler404(request, exception):
    Info = InformationsForTemplate(request)
    return render(request, 'facades/404.html', context=Info,status=404)
#----------------------------------------------------------------------------------------------