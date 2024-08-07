from datetime import datetime

from rest_framework import status
from rest_framework.generics import UpdateAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Sale
from apps.models import Category, Debtors, Warehouse, ManagerAdmin
from apps.serializer import CategorySerializer, ProductSerializer, DebtorsSerializer, WarehouseModelSerializer, \
    ManagerAdminSerializer


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


class DailyBenefitView(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get(self, request, date_str, format=None):
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            sales = Sale.objects.filter(date=date)
            daily_benefit = 0

            for sale in sales:
                daily_benefit += sale.quantity * sale.product.benefit

            return Response({'date': date, 'daily_benefit': daily_benefit}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
