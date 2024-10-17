from http.client import HTTPResponse
from django.shortcuts import redirect, render
from shop.form import CustomUserForm
from .models import *
from django.contrib import messages
 
def home(request):
    products=Product.objects.filter(trending=1)
    catagory=Catagory.objects.filter(status=0)
    return render(request,'shop/catagory.html',{'catagory':catagory,'products':products})
def register(request):
    form=CustomUserForm()
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