from django.utils import timezone
from django.db import models
import uuid

# Create your models here.
class BaseTrackedModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseTrackedModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subcategories'
    )

    def __str__(self):
        return self.name

    def full_path(self):
        path = [self.name]
        parent = self.parent
        while parent:
            path.append(parent.name)
            parent = parent.parent
        return " → ".join(reversed(path))

class Warehouse(BaseTrackedModel):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    manager_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Product(BaseTrackedModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    warehouses = models.ManyToManyField(Warehouse, through='InventoryRecord')

    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return self.name

class InventoryRecord(BaseTrackedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    last_restock = models.DateTimeField()
    min_required = models.IntegerField()

    class Meta:
        unique_together = ('product', 'warehouse')

    def is_below_minimum(self):
        return self.quantity < self.min_required

    def __str__(self):
        return f"{self.product} @ {self.warehouse}"
