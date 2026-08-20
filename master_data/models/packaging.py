import uuid

from django.db import models

from .category import Category
from .supplier import Supplier


class Packaging(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        to_field="name",
        db_column="category_name",
        related_name="packaging_items",
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        to_field="contact_person",
        db_column="supplier_contact",
        related_name="packaging_items",
    )

    discontinued = models.BooleanField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    low_stock_value = models.IntegerField(
        default=10,
    )

    class Meta:
        db_table = "packaging_static"

    def __str__(self):
        return self.name