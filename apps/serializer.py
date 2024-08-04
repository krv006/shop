from rest_framework.serializers import ModelSerializer, SerializerMethodField, ReadOnlyField
from apps.models import Category, Product, Debtors, Warehouse

from decimal import Decimal
import requests


class ParentCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name',


class CategorySerializer(ModelSerializer):
    parent = ParentCategorySerializer(read_only=True)

    class Meta:
        model = Category
        fields = 'id', 'name', 'parent',


class ProductSerializer(ModelSerializer):
    category = SerializerMethodField()
    price_usd = SerializerMethodField()
    price_uzs = SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id', 'description', 'quantity', 'price_usd', 'price_uzs', 'arrival_price', 'benefit', 'category',

    def get_category(self, obj):
        if obj.category.children.exists():
            return {"category": CategorySerializer(obj.category).data}
        return obj.category.name

    def get_price_usd(self, obj):
        amount = Decimal(obj.departure_price)
        from_currency = 'USD'
        to_currency = 'UZS'
        conversion_rate = self.get_conversion_rate(from_currency, to_currency)
        if conversion_rate is None:
            return None
        converted_amount = amount / Decimal(conversion_rate)
        return converted_amount

    def get_price_uzs(self, obj):
        return obj.departure_price

    def get_conversion_rate(self, from_currency, to_currency):
        API_ENDPOINT = "https://v6.exchangerate-api.com/v6/0f84fd60fa278bb9b3c8e126/latest/{}".format(from_currency)
        response = requests.get(API_ENDPOINT)
        data = response.json()
        return Decimal(data['conversion_rates'].get(to_currency, 0))


class DebtorsSerializer(ModelSerializer):
    class Meta:
        model = Debtors
        fields = 'id', 'full_name', 'phone_number', 'date', 'price',


# "category"{
#     "category" : "askjfvbs"
# }


class WarehouseModelSerializer(ModelSerializer):
    class Meta:
        model = Warehouse
        fields = 'name', 'price'
