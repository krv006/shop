import uuid

from django.db.models import Model, DateTimeField, UUIDField, TextField, CharField, IntegerField, ForeignKey, CASCADE, \
    BooleanField
from mptt.models import MPTTModel, TreeForeignKey


class CreatedAtBase(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Base(CreatedAtBase):
    # id = UUIDField(primary_key=True, db_default=RandomUUID(), editable=False) # postgres da ishlatiladi
    id = UUIDField(default=uuid.uuid4, primary_key=True)  # sqlite uchun basic

    class Meta:
        abstract = True


class Category(MPTTModel, CreatedAtBase):
    name = CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name


class Product(Base, CreatedAtBase):
    name = CharField(max_length=255)
    description = TextField()
    price = IntegerField()
    category = ForeignKey('apps.Category', CASCADE, related_name='category')
    is_premium = BooleanField(default=False)

    def __str__(self):
        return self.name


class Warehouse(Model):
    name = CharField(max_length=255)
    price = IntegerField()

    def __str__(self):
        return self.name

