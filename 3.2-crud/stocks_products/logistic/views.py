from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer

class ProductPagination(PageNumberPagination):
    page_size = 10

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']  # Поиск по названию и описанию продукта

class StockPagination(PageNumberPagination):
    page_size = 5

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = StockPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]

    # Настраиваем поиск по названию или описанию продукта, связанного со складом
    search_fields = ['positions__product__title', 'positions__product__description']
