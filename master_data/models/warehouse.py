import uuid

from django.db import models

from .raw_material import RawMaterial
from .finished_product import FinishedProduct
from .packaging import Packaging


class RawMaterialWarehouse(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    raw_material = models.ForeignKey(
        RawMaterial,
        on_delete=models.CASCADE,
        db_column="raw_material_id",
        related_name="warehouses",
    )

    warehouse = models.CharField(
        max_length=255,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "raw_materials_warehouses"

    def __str__(self):
        return f"{self.raw_material.name} - {self.warehouse}"


class FinishedProductWarehouse(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    finished_product = models.ForeignKey(
        FinishedProduct,
        on_delete=models.CASCADE,
        db_column="finished_product_id",
        related_name="warehouses",
    )

    warehouse = models.CharField(
        max_length=255,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "finished_products_warehouses"

    def __str__(self):
        return f"{self.finished_product.name} - {self.warehouse}"


class PackagingWarehouse(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    packaging = models.ForeignKey(
        Packaging,
        on_delete=models.CASCADE,
        db_column="packaging_id",
        related_name="warehouses",
    )

    warehouse = models.CharField(
        max_length=255,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "packaging_warehouses"

    def __str__(self):
        return f"{self.packaging.name} - {self.warehouse}"