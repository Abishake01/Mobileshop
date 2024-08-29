from django.shortcuts import render
from .models import *

def home(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,'shop/index.html',{'catagory':catagory})
def register(request):
    return render(request,'shop/register.html')
