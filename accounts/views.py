from django.shortcuts import render,redirect
from .forms import *
from  django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .models import *
from django.shortcuts import render,get_object_or_404
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,phoneNumber=cd['phoneNumber'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'you logged in successfully','success')
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                else:
                    return redirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request,'username or password is wrong','alert')

    Loginform = UserLoginForm()
    Registerform = UserCreationForm()      
    return render(request, 'accounts/login.html', {'Loginform': Loginform,'Registerform': Registerform})
#------------------------------------------------------------------------------------------------
def profile(request):
    if request.method == 'POST':
        profileForm = UserChangeForm(request.POST,instance=request.user)

        if profileForm.is_valid():
            profileForm.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        profileForm = UserChangeForm(instance=request.user)

    return render(request, 'facades/dashboard.html', {'profileForm': profileForm})
#------------------------------------------------------------------------------------------------
def user_logout(request):
    logout(request)
    messages.success(request,'you logged out successfully','success')
    return redirect('facades:home')
#------------------------------------------------------------------------------------------------
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'ثبت نام شما با موفقیت انجام شد.', 'success')
            user = authenticate(request, username=form.cleaned_data['phoneNumber'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('facades:home')
        else:
            messages.error(request, 'خطا در ثبت نام.', 'alert')
    
    Loginform = UserLoginForm()
    Registerform = UserCreationForm()
    return render(request, 'accounts/login.html', {'Loginform': Loginform,'Registerform': Registerform})
#------------------------------------------------------------------------------------------------
def AddToWish(request, id):
    if(request.user.is_authenticated):
        item = get_object_or_404(Product, id=id)

        request.user.wishlist.add(item)

        # return redirect('stuff:product_detail',item.slug,item.id)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("accounts:login")
#------------------------------------------------------------------------------------------------
def RomeveToWish(request, id):
    if(request.user.is_authenticated):
        item = get_object_or_404(Product, id=id)

        request.user.wishlist.remove(item)

        # return redirect('stuff:product_detail',item.slug,item.id)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("accounts:login")
#------------------------------------------------------------------------------------------------
def LikeComment(request, id):
    if(request.user.is_authenticated):
        comment = get_object_or_404(Comment, id=id)

        comment.likes.add(request.user)
        comment.dislikes.remove(request.user)
        

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("accounts:login")
#------------------------------------------------------------------------------------------------
def DisLikeComment(request, id):
    if(request.user.is_authenticated):
        comment = get_object_or_404(Comment, id=id)

        comment.dislikes.add(request.user)
        comment.likes.remove(request.user)
        
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("accounts:login")
#------------------------------------------------------------------------------------------------
# @login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.phone_number = request.user.phoneNumber
            address.user = request.user
            address.save()
            messages.success(request, 'آدرس با موفقیت ثبت شد.', 'success')
            return redirect('facades:dashboard')
    else:
        form = AddressForm()
    return redirect('facades:dashboard')
#------------------------------------------------------------------------------------------------
def delete_address(request,address_id):
    address = get_object_or_404(Address,id=address_id)
    address.delete()
    messages.success(request,'با موفقیت آدرس حذف شد.','background-color: #00ac09;')
    return redirect('facades:dashboard')
#------------------------------------------------------------------------------------------------