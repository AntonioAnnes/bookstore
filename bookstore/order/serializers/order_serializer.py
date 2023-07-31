from rest_framework import serializers

from bookstore.product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

class Meta:
    model = Product
    fields = ['product', 'total']