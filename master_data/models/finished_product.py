import uuid

from django.db import models

from .category import Category


class FinishedProduct(models.Model):
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
        related_name="finished_products",
    )

    discontinued = models.BooleanField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    low_stock_value = models.IntegerField(
        default=10,
    )

    class Meta:
        db_table = "finished_products_static"

    def __str__(self):
        return self.name