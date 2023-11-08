from django.db import models
from stdimage import StdImageField
from my_auth.models import CustomUser


# Create your models here.

def upload_to(instance, filename):
    return f"images/{filename}"


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = StdImageField(upload_to=upload_to, variations={'thumbnail': (200, 200)}, blank=True, null=True)

    def __str__(self):
        return self.name


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
