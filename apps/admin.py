from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from apps.models import Category, Product, Debtors, Warehouse


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Debtors)
class DebtorsAdmin(admin.ModelAdmin):
    pass


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    pass
