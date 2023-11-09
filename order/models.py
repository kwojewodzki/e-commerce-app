from django.db import models
from my_auth.models import CustomUser
from product.models import Product


# Create your models here.


class Address(models.Model):
    city = models.CharField(max_length=64)
    street_name = models.CharField(max_length=64)
    building_number = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.city}, {self.street_name} {self.building_number}"


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.amount} of {self.product.name}"

    def get_total_item_price(self):
        return self.product.price * self.amount


class Order(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    product_list = models.ManyToManyField(OrderProduct)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateTimeField()
    total_price = models.FloatField()

    def __str__(self):
        return f"An order of {self.client.username} from {self.order_date}"
