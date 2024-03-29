from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Product, Category, Brand
from .scripts import formating_price
from accounts.forms import CommentForm
from accounts.models import WatchedProduct
from facades.views import InformationsForTemplate
#-----------------------------------------------------------------------------------
pagination_amount = 12
#-----------------------------------------------------------------------------------
def ordering(request,product_list):

    order_option = request.POST.get("ordering")

    if(order_option == "popularity"):
        return product_list.order_by('-rating')
    elif(order_option == "expensive"):
        return product_list.order_by('-price')
    elif(order_option == "cheap"):
        return product_list.order_by('price')
    else:
        return product_list.order_by('updated')

#-----------------------------------------------------------------------------------
def filter(request,product_list):
    filter_price_option = -1
    brands = []
    rating_list  = []
    filters = {}
    filters["active"] = False

    if(request.method == "POST"):
        keys = request.POST.keys()

        #get brand id and star ints
        for key in keys:
            if 'brand-' in key:
                brands.append(int(key[6]))
            if 'cus-rating-' in key:
                rating_list.append(int(key[11]))  


        filter_price_option = request.POST.get("filter-price")
        if filter_price_option:
            filter_price_option = int(filter_price_option)

            filter_price_high = 250 * 2 ** (filter_price_option - 1) * 1000
            filter_price_low = filter_price_high // 2

            if(filter_price_option == 1):
                filter_price_low = 0

            if(filter_price_option == 5):
                filter_price_high = 100000000
                filter_price_low = 2000000
        
    
    if(filter_price_option != -1 and filter_price_option):
        product_list = product_list.filter(price__gte=filter_price_low, price__lte=filter_price_high)
        filters['price_bool'] = True
        filters['price_high'] = formating_price(filter_price_high)
        filters['price_low'] = formating_price(filter_price_low)
        filters["active"] = True



    if(len(brands) != 0):
        product_list = product_list.filter(brand_id__in=brands)
        filters['brand_bool'] = True
        brands_name = []
        for brand_id in brands:
            brands_name.append(Brand.objects.get(id=brand_id).name)
        filters['brands'] = brands_name
        filters["active"] = True

    if rating_list:
        filter_criteria = Q()
        for rating in rating_list:
            filter_criteria |= Q(rating=rating)
        product_list = product_list.filter(filter_criteria)

        filters['rating_bool'] = True
        ratings = []
        for rate in rating_list:
            ratings.append(rate * 20)
        filters['ratings'] = ratings
        filters["active"] = True

    filters["product_list"] = product_list


    filters["rating_count"] = {
        "1" : product_list.filter(rating=1).count(),
        "2" : product_list.filter(rating=2).count(),
        "3" : product_list.filter(rating=3).count(),
        "4" : product_list.filter(rating=4).count(),
        "5" : product_list.filter(rating=5).count(),
    }

    

    return filters
#-----------------------------------------------------------------------------------
def product_detail(request, slug,id):
    product = get_object_or_404(Product, id=id,slug=slug)

    Suggested = product.get_similar_products()
    comments = product.get_comments()


    if request.user.is_authenticated:
        watched_product, created = WatchedProduct.objects.get_or_create(user=request.user, product=product)
        if not created:
            watched_product.timestamp = timezone.now()
            watched_product.save()


    AddCommentForm = CommentForm()

    Info = InformationsForTemplate(request)
    Info.update({'product': product,'Suggested':Suggested,'CommentForm':AddCommentForm,'comments':comments})
    
    return render(request,'stuff/product.html',Info) 
#-----------------------------------------------------------------------------------
def product_search(request,page):
    query = request.GET.get('query')
    product_list = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    filters = filter(request,product_list)
    product_list = ordering(request,filters["product_list"])

    paginator = Paginator(product_list, pagination_amount)
    product_list = paginator.get_page(page)

    Info = InformationsForTemplate(request)
    Info.update({'products': product_list,'query':query,'paginator':paginator,'filters':filters})

    return render(request, 'stuff/bonePage.html', Info)
#-----------------------------------------------------------------------------------
def Category_detail(request,id,page):
    category = get_object_or_404(Category, id=id)
    product_list = category.products.all()

    filters = filter(request,product_list)
    product_list = ordering(request,filters["product_list"])

    paginator = Paginator(product_list, pagination_amount)
    product_list = paginator.get_page(page)


    Info = InformationsForTemplate(request)
    Info.update({'products': product_list,'category':category,'paginator':paginator,'filters':filters})

    return render(request,'stuff/bonePage.html',Info)
#-----------------------------------------------------------------------------------
def showWishList(request,page):
    wishlistProducts = request.user.wishlist.all()
    filters = filter(request,wishlistProducts)
    wishlistProducts = ordering(request,filters["product_list"])

    paginator = Paginator(wishlistProducts, pagination_amount)
    product_list = paginator.get_page(page)


    Info = InformationsForTemplate(request)
    Info.update({'products': product_list,'paginator':paginator,'filters':filters})

    return render(request,'stuff/bonePage.html',Info)
#-----------------------------------------------------------------------------------