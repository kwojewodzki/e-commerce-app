from django.contrib import admin
from .models import ProductCategory, Product, Order, OrderProduct, Address

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(OrderProduct)
admin.site.register(Order)
