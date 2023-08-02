from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from bookstore.order.models import Order
from bookstore.order.serializers import OrderSerializer
from bookstore.product.serializers import ProductSerializer


class OrderViewSet(ModelViewSet):
        authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
        permission_classes = [IsAuthenticated]
        serializer_class = ProductSerializer

    serializer_class = OrderSerializer
    queryset = Order.objects.all()