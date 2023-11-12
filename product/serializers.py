from rest_framework import serializers
from order.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "image"
        ]


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "category",
            "price",
            "image"
        ]


class GetStatisticsSerializer(serializers.Serializer):
    start_date = serializers.DateField(write_only=True)
    end_date = serializers.DateField(write_only=True)
    count = serializers.IntegerField(write_only=True)
    product_list = serializers.ListField(read_only=True)
