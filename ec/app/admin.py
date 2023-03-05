from . models import Cart, Customer, Product
from django.contrib import admin

# Register your models here.
@admin.register(Product)

class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id','title','discounted_price','categoty','product_image']


@admin.register(Customer)

class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id','user','locality','city','state','zipcode']


