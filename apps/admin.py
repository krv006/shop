from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.models import Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    pass
