from http.client import HTTPResponse
import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from shop.form import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
 
def home(request):
    products=Product.objects.filter(trending=1)
    catagory=Catagory.objects.filter(status=0)
    return render(request,'shop/catagory.html',{'catagory':catagory,'products':products})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout success")
    return redirect('/home')
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
     if request.method=='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in Successfully")
            return redirect('/')
        else:
            messages.error(request,"Invalid User Name Or Password")
            return redirect('/login')
     return render(request,'shop/login.html')
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Success')
            return redirect('/login')
    return render(request,'shop/register.html',{'form':form})

def mobileviews(request,name):
    
    if (Catagory.objects.filter(name=name,status=0)): 
        products=Product.objects.filter(category__name=name)
        return render(request,'shop/products/index.html',{'products':products,'category_name':name})
    else:
        messages.error(request,"No such Product Found")
        return redirect('home')
    
    
def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,'shop/products/product_details.html',{'products':products})
        else:
            messages.error(request,'No such Category Found')
            return redirect('home')
    else:
        messages.error(request,'No such Category Found')

def brand(request, bname):
 
    brand = Brands.objects.filter(brand_name=bname,).first()
    return render(request, 'shop/catagory.html', {'brand': brand})

def service_page(request):
    return render(request, 'shop/service.html')

def about_page(request):
    return render(request,'shop/about.html')

def Contact_page(request):
    return render(request,'shop/contact.html')

def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            return JsonResponse({'status':'Product Add to Cart Success'}, status=200)
        else:
            return JsonResponse({'status':'Login to Add Cart'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)