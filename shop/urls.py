 
from django.urls import path
from . import views



urlpatterns = [
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    #path('home/<str:catagory>/',views.mobileviews,name='mobileviews'),
    path('home/<str:name>/', views.mobileviews, name='mobileviews'),
    path('home/<str:name>/', views.brand, name='brand'),
    path('home/<str:cname>/<str:pname>', views.product_details, name='product_details'),
    path('service/', views.service_page, name='service'),
    path('about/',views.about_page,name='about'),
    path('contact',views.Contact_page,name='contact'),
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