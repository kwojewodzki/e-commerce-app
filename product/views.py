from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend

from order.models import Order, OrderProduct
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
    queryset = Product.objects.all()
    permission_classes = (IsSeller,)
    lookup_field = 'pk'


class GetStatisticsAPIView(generics.ListAPIView):
    serializer_class = GetStatisticsSerializer
    permission_classes = (IsSeller,)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["start_date"] = self.kwargs['start_date']
        context["end_date"] = self.kwargs['end_date']
        return context

    def get_queryset(self):
        start_date, end_date, count = self.kwargs.values()
        orders = Order.objects.filter(order_date__range=(start_date, end_date))
        products_and_amount = OrderProduct.objects.filter(order__in=orders).values('product').annotate(
            Sum('amount')).order_by('-amount__sum')
        if count > len(products_and_amount):
            return products_and_amount
        return products_and_amount[:count]
