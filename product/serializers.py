from rest_framework import serializers
from order.models import Product
from product.models import ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateModifySerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "category",
            "price",
            "image",
            "thumbnail"
        ]

    def create(self, validated_data):
        new_product = super().create(validated_data)
        new_product.get_thumbnail()
        return new_product


class GetStatisticsSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField(read_only=True)
    amount = serializers.SerializerMethodField(read_only=True)

    def get_product(self, obj):
        return Product.objects.filter(pk=obj['product']).values()

    def get_amount(self, obj):
        return obj['amount__sum']

    class Meta:
        model = Product
        fields = [
            "product",
            "amount",
        ]
