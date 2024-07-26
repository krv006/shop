from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product, Warehouse


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name', 'parent'

