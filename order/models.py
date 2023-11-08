from django.db import models
from stdimage import StdImageField


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
