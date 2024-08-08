import uuid

from django.db.models import Model, DateTimeField, UUIDField, TextField, CharField, IntegerField, ForeignKey, CASCADE, \
    DateField, DecimalField, ManyToManyField, PositiveIntegerField, TextChoices
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


class Category(MPTTModel, CreatedAtBase):  # category
    name = CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name


class Product(Base):  # product
    name = CharField(max_length=255)
    description = TextField()
    arrival_price = IntegerField()  # kelish
    departure_price = IntegerField()  # ketish
    quantity = PositiveIntegerField()
    category = ForeignKey(Category, on_delete=CASCADE, related_name='category')

    def __str__(self):
        return self.name

    @property
    def benefit(self):
        return self.departure_price - self.arrival_price


class Sale(Model):
    class SaleMethod(TextChoices):
        TODAY = 'today', 'Today'
        THREE_DAY = 'three-day', 'Three-day'
        WEEK = 'week', 'Week'
        MONTH = 'month', 'Month'
        YEAR = 'year', 'Year'

    product = ForeignKey(Product, on_delete=CASCADE, related_name='sales')
    sale_method = CharField(max_length=255, choices=SaleMethod)
    created_at = DateTimeField(auto_now_add=True)  # Qo'shilgan sana


class Warehouse(Base):  # sklad
    name = CharField(max_length=255)
    price = IntegerField()

    def __str__(self):
        return self.name


class Debtors(Base):  # qarizdorlar
    full_name = CharField(max_length=250)
    phone_number = CharField(max_length=250, blank=True)
    product = ManyToManyField('apps.Product', related_name='debtor_product')
    date = DateField(auto_now_add=True)
    price = DecimalField(max_digits=11, decimal_places=3)

    def __str__(self):
        return self.full_name


class ManagerAdmin(Model):
    product = ForeignKey('apps.Product', CASCADE)

    @property
    def amount_benefit(self):
        products = Product.objects.all()
        total_benefit = sum(product.benefit for product in products)
        return total_benefit
