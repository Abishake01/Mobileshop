from http.client import HTTPResponse
import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from shop.form import ContactForm, CustomUserForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q


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
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect('/home')
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect('/login')
        return render(request, 'shop/login.html')

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Success')
            return redirect('/login')
    return render(request,'shop/register.html',{'form':form})

def profile_page(request):
    pass
def password_change(request):
    pass
def offer_page(request):
    products=Product.objects.filter(trending=1)
    return render(request,'shop/offers.html',{'products':products})

def search_products(request):
    query = request.GET.get('q')
    if query:
        # Filter by product name, category name (related field), or description
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |  # Filter by related category name
            Q(description__icontains=query)
        )
    else:
        products = Product.objects.none()  # No results if the query is empty
    
    return render(request, 'shop/search_results.html', {'products': products, 'query': query})
@login_required
def buy_view(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/buy.html', {'product': product})

@login_required
def place_order_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        shipping_address = request.POST.get('shipping_address')
        phone_number = request.POST.get('phone_number')

        product = Product.objects.get(id=product_id)
        order = Order.objects.create(
            user=request.user,
            product=product,
            shipping_address=shipping_address,
            phone_number=phone_number,
            total_amount=product.selling_price
        )

        # Redirect to the order confirmation page
        return redirect('order_placed', order_id=order.id)
    
@login_required
def order_placed_view(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'shop/order_placed.html', {'order': order})  
    
def mobileviews(request,name):
    
    if (Catagory.objects.filter(name=name,status=0)): 
        products=Product.objects.filter(category__name=name)
        return render(request,'shop/products/main.html',{'products':products,'category_name':name})
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
 
class service_page(View):
 def get(self,request):
    if request.method == 'POST':
        return  redirect('/home')
    else:
        return render(request, 'shop/service.html')

def about_page(request):
    return render(request,'shop/about.html')

def Contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Construct the email
        subject = f'New Message from {name}'
        body = f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}'

        try:
            # Replace with your admin email
            admin_email = 'abishake381@gmail.com'  # Your admin email address

            # Send the email
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,  # From email (your email)
                [admin_email],  # To email (admin email)
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('/contact')  # Redirect to the contact page after success
        except Exception as e:
            messages.error(request, 'Failed to send your message. Please try again later.')
            print(e)  # Log the exception for debugging

    return render(request, 'shop/contact.html')


def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            try:
                data = json.loads(request.body)   
                product_qty = data.get('product_qty')
                product_id = data.get('pid')
                
                # Check if product exists
                product = Product.objects.get(id=product_id)
                
                if product:
                     
                    if Cart.objects.filter(user=request.user, product_id=product_id).exists():
                        return JsonResponse({'status': 'Product Already in Cart'}, status=200)
                    else:
                       
                        if product.quantity >= product_qty:
                            Cart.objects.create(user=request.user, product=product, product_qty=product_qty)
                            return JsonResponse({'status': 'Product Added to Cart Successfully'}, status=200)
                        else:
                            return JsonResponse({'status': 'Product Stock Not Available'}, status=200)
            except Product.DoesNotExist:
                return JsonResponse({'status': 'Product Not Found'}, status=404)
        else:
            return JsonResponse({'status': 'Login to Add to Cart'}, status=200)
    else:
        return JsonResponse({'status': 'Invalid Access'}, status=400)
    
def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        
        return render(request,'shop/cart.html',{'cart':cart})
    else:
       return redirect('/home')
   
def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect('/cart')

def fav_page(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            product_id = data.get('pid')
            product_status = Product.objects.get(id=product_id)

            if product_status:
                if Favourite.objects.filter(user=request.user, product_id=product_id).exists():
                    return JsonResponse({'status': 'Product Already in Favourite'}, status=200)
                else:
                    Favourite.objects.create(user=request.user, product_id=product_id)
                    return JsonResponse({'status': 'Added to Favourite'}, status=200)
        else:
            return JsonResponse({'status': 'Login to Add to Favourite'}, status=403)
    else:
        return JsonResponse({'status': 'Invalid Access'}, status=400)

def favviewpage(request):
    if request.user.is_authenticated:
        fav=Favourite.objects.filter(user=request.user)
        return render(request,'shop/fav.html',{'fav':fav})
    else:
       return redirect('/home')
   
def remove_fav(request,fid):
    favitem=Favourite.objects.get(id=fid)
    favitem.delete()
    return redirect('/favviewpage')