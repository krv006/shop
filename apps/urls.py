from django.urls import path
from apps.views import CategoryListAPIView, ProductListAPIView

urlpatterns = [
    path("category", CategoryListAPIView.as_view()),
    path("product", ProductListAPIView.as_view()),
]
