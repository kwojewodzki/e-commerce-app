from django.core.mail import send_mail
from rest_framework.response import Response

from rest_framework import generics, status
from .models import Order
from product.permissions import IsCustomer
from .serializers import CreateOrderSerializer


# Create your views here.


class CreateOrderAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_classes = (IsCustomer,)
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data, context={'request': request})
        message = "Your order was successfully placed. Thank You"
        if serializer.is_valid():
            serializer.save()
            send_mail("Confirmation",
                      message,
                      from_email="confirmation@ecommerce.com",
                      recipient_list=[request.user.email])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
