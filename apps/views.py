from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from apps.models import Category, Product, Debtors
from apps.serializer import CategorySerializer, ProductSerializer, DebtorsSerializer

from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = Pagination


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DebtorsListAPIView(ListAPIView):
    queryset = Debtors.objects.all()
    serializer_class = DebtorsSerializer
    pagination_class = Pagination


class DebtorsCreateAPIView(CreateAPIView):
    queryset = Debtors.objects.all()
    serializer_class = DebtorsSerializer


class DebtorsUpdateAPIView(UpdateAPIView):
    queryset = Debtors.objects.all()
    serializer_class = DebtorsSerializer
