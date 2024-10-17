from django.contrib import admin
from .models import Catagory
from .models import Product
from .models import Brands

#class CatagoryAdmin(admin.ModelAdmin):
   # list_display=('name','image','description')
    
admin.site.register(Catagory)#,CatagoryAdmin
admin.site.register(Product)
admin.site.register(Brands)