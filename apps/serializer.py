from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product, Debtors


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name', 'parent'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = 'id', 'description', 'price', 'category'


class DebtorsSerializer(ModelSerializer):
    class Meta:
        model = Debtors
        fields = 'id', 'full_name', 'phone_number', 'date', 'price'
