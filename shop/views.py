from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
 
def home(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,'shop/index.html',{'catagory':catagory})
def register(request):
    return render(request,'shop/register.html')
def mobileviews(request,name):
    if (Catagory.objects.filter(name=name,status=0)): 
        products=Product.objects.filter(category__name=name)
        return render(request,'shop/products/index.html',{'products':products,'category_name':name})
    else:
        messages.error(request,"No such Product Found")
        return redirect('home')
    
    
    