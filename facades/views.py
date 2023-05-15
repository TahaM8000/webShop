from django.shortcuts import render
from stuff.models import Product


#----------------------------------------------------------------------------------------------
def HomePage(request):
    print("--------------------------")
    # discounted stuff
    discounted = Product.objects.filter(available=True,discounted=True)

    # New stuff in website
    news = Product.objects.filter(available=True)
    news_list = [s.id for s in news if s.is_new]
    print(news_list)
    news = news.filter(id__in=news_list)




    # return render(request,'facades/landing.html')
    return render(request,'facades/landing.html',{'products':news,'productsOfDiscount':discounted,})
#----------------------------------------------------------------------------------------------
