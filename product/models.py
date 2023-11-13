from django.db import models

from io import BytesIO
from PIL import Image
from django.core.files import File


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
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.name

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()

            return self.thumbnail.url

    @staticmethod
    def get_image_name(name: str):
        name = name.split("/")[-1]
        return 'thumbnails/' + name

    def make_thumbnail(self, image):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail((200, 200))

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=self.get_image_name(image.name))

        return thumbnail
