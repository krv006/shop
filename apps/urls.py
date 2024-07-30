from django.urls import path
from apps.views import CategoryListAPIView, ProductListAPIView, DebtorsCreateAPIView, DebtorsUpdateAPIView, \
    ProductCreateAPIView, ProductUpdateAPIView, DebtorsListAPIView

urlpatterns = [
    path("category", CategoryListAPIView.as_view()),

    path("product", ProductListAPIView.as_view()),
    path("product/<int:pk>", ProductCreateAPIView.as_view()),
    path("product/<int:pk>", ProductUpdateAPIView.as_view()),

    
    path("debtors", DebtorsListAPIView.as_view()),
    path("debtors/<int:pk>", DebtorsUpdateAPIView.as_view()),
    path("debtors/<int:pk>", DebtorsCreateAPIView.as_view()),
]
