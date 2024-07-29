from django.urls import path
from apps.views import CategoryListAPIView, ProductListAPIView, DebtorsCreateAPIView

urlpatterns = [
    path("category", CategoryListAPIView.as_view()),
    path("product", ProductListAPIView.as_view()),
    path("debtors", DebtorsCreateAPIView.as_view()),
]
