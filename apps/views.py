from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView

from apps.models import Category
from apps.serializer import CategorySerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category
    serializer_class = CategorySerializer
