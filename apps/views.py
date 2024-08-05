from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from apps.models import Category, Product, Debtors, Warehouse, ManagerAdmin
from apps.serializer import CategorySerializer, ProductSerializer, DebtorsSerializer, WarehouseModelSerializer, \
    ManagerAdminSerializer

from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = Pagination


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DebtorsListCreateAPIView(ListCreateAPIView):
    queryset = Debtors.objects.all()
    serializer_class = DebtorsSerializer
    pagination_class = Pagination


class DebtorsUpdateAPIView(UpdateAPIView):
    queryset = Debtors.objects.all()
    serializer_class = DebtorsSerializer


class WarehouseListCreateAPIView(ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseModelSerializer


class ManagerAdminListCreateView(ListCreateAPIView):
    queryset = ManagerAdmin.objects.all()
    serializer_class = ManagerAdminSerializer


class ManagerAdminRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ManagerAdmin.objects.all()
    serializer_class = ManagerAdminSerializer
