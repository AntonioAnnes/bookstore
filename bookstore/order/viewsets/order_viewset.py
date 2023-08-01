
from rest_framework.viewsets import ModelViewSet

from bookstore.order.models import Order
from bookstore.order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()