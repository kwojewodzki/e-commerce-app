from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from my_auth.models import CustomUser
from order.models import Order, OrderProduct
from product.models import Product
from datetime import date, timedelta


def calculate_total_price(instance):
    total = 0
    order_products = OrderProduct.objects.filter(order=instance).all()
    for item in order_products:
        total += item.get_total_item_price()
    return total


class CreateOrderSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=64, write_only=True)
    surname = serializers.CharField(max_length=64, write_only=True)
    products = serializers.JSONField(write_only=True)
    address = serializers.CharField(write_only=True)

    class Meta:
        model = Order
        fields = (
            'name',
            'surname',
            'products',
            'address',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['payment_date'] = instance.payment_date
        representation['total_price'] = calculate_total_price(instance)
        return representation

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        new_order = Order.objects.create(
            client=user,
            address=validated_data["address"],
            payment_date=date.today() + timedelta(days=5),
        )

        for product_id, amount in validated_data['products'].items():
            try:
                product = Product.objects.get(pk=int(product_id))
            except Product.DoesNotExist:
                product = None

            OrderProduct.objects.create(
                order=new_order,
                product=product,
                amount=amount,
            )
        return new_order
