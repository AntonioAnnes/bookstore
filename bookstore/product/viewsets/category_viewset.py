from rest_framework.viewsets import ModelViewSet

from bookstore.product.models import Category
from bookstore.product.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().order_by("id")