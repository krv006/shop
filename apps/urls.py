from django.urls import path
from apps.views import ProductListCreateAPIView, DebtorsUpdateAPIView, \
    ProductUpdateAPIView, DebtorsListCreateAPIView, CategoryListCreateAPIView, WarehouseListCreateAPIView

urlpatterns = [
    path("category", CategoryListCreateAPIView.as_view()),

    path("product", ProductListCreateAPIView.as_view()),
    path("product/update/<int:pk>", ProductUpdateAPIView.as_view()),

    path("debtors", DebtorsListCreateAPIView.as_view()),
    path("debtors/<int:pk>", DebtorsUpdateAPIView.as_view()),

    path("warehouse", WarehouseListCreateAPIView.as_view()),

]
