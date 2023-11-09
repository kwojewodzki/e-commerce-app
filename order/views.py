from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from product.serializers import ProductSerializer, ProductCreateSerializer
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from .models import Order
from product.paginations import ProductListPagination
from product.permissions import IsCustomer
from .serializers import CreateOrderSerializer


# Create your views here.


class CreateOrderAPIView(generics.CreateAPIView): #TODO add sending email
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_classes = (IsCustomer,)
    lookup_field = 'pk'

