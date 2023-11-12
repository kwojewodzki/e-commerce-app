from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ProductSerializer, ProductCreateSerializer, GetStatisticsSerializer
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from .models import Product
from product.paginations import ProductListPagination
from .permissions import IsSeller


# Create your views here.

class ListProductsAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    pagination_class = ProductListPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'category', 'description', 'price']
    ordering_fields = ['name', 'category', 'price']


class DetailProductAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    lookup_field = 'pk'


class CreateProductAPIView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()
    permission_classes = (IsSeller,)


class UpdateDeleteProductAPIView(generics.DestroyAPIView, generics.UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsSeller,)
    lookup_field = 'pk'


class GetStatisticsAPIView(generics.ListAPIView):
    serializer_class = GetStatisticsSerializer
    queryset = Product.objects.all()
    permission_classes = (IsSeller,)
