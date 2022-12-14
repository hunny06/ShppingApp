from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","user","name","city","state","zipcode","locality"]
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","selling_price","discount_price","discription","brand","category","product_image"]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user","product","quantity"]
    
@admin.register(OrderPlace)
class OrderPlaceAdmin(admin.ModelAdmin):
    list_display = ["user","product","customer","order_date","quantity","status"]
