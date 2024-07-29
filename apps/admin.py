# from parler.admin import TranslatableAdmin
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from apps.models import Category, Product


# Register your models here.
# @admin.register(Category)
# class CategoryAdmin(TranslatableAdmin):
#     pass


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    pass


@admin.register(Product)
class ProductAdmin(DraggableMPTTAdmin):
    pass
