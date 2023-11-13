from django.contrib import admin
from .models import Order, OrderProduct, Address

# Register your models here.

admin.site.register(Address)
admin.site.register(OrderProduct)
admin.site.register(Order)
