from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from apps.models import Category, Product, Debtors
from apps.serializer import CategorySerializer, ProductSerializer, DebtorsSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DebtorsCreateAPIView(CreateAPIView):
    queryset = Debtors.objects.all()
    serializer_class = DebtorsSerializer


class DebtorsUpdateAPIView(UpdateAPIView):
    queryset = Debtors.objects.all()
    serializer_class = DebtorsSerializer
