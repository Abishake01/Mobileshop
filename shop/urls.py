 
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    #path('home/<str:catagory>/',views.mobileviews,name='mobileviews'),
    path('home/<str:name>/', views.mobileviews, name='mobileviews'),
]