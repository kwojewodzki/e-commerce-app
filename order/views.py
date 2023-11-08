from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ProductListSerializer
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from .models import Product
from .paginations import ProductListPagination


# Create your views here.

class ListProductsAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    pagination_class = ProductListPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'category', 'description', 'price']
    ordering_fields = ['name', 'category', 'price']


class DetailProductAPIView(generics.RetrieveAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    lookup_field = 'pk'
