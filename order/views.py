from .serializers import ProductListSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Product


# Create your views here.

class ListProductsAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
