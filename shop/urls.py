 
from django.urls import path
from . import views 



urlpatterns = [
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('cart',views.cart_page,name='cart'),
    path('fav',views.fav_page,name='fav'),
    path('favviewpage',views.favviewpage,name='favviewpage'),
    path('remove_fav/<int:fid>',views.remove_fav,name='remove_fav'),
    path('remove_cart/<int:cid>',views.remove_cart,name='remove_cart'),
    #path('home/<str:catagory>/',views.mobileviews,name='mobileviews'),
    path('home/<str:name>/', views.mobileviews, name='mobileviews'),
    path('home/<str:name>/', views.brand, name='brand'),
    path('home/<str:cname>/<str:pname>', views.product_details, name='product_details'),
    path('service/', views.service_page, name='service'),
    path('about/',views.about_page,name='about'),
    path('contact/',views.Contact_page,name='contact'),
    path('addtocart',views.add_to_cart,name='addtocart'),
]
'''
urlpatterns = [
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    #path('home/<str:catagory>/',views.mobileviews,name='mobileviews'),
    path('home/<str:name>/', views.mobileviews, name='mobileviews'),
    path('home/<str:name>/', views.brand, name='brand'),
    path('home/<str:cname>/<str:pname>', views.product_details, name='product_details'),
]
'''