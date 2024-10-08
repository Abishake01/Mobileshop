from http.client import HTTPResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
 
def home(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,'shop/catagory.html',{'catagory':catagory})
def register(request):
    return render(request,'shop/register.html')
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
        return redirect('home')
    
    