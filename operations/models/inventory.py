import uuid

from django.db import models

from master_data.models import (
    RawMaterial,
    FinishedProduct,
    Packaging,
)

class RawMaterialInventory(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
    )

    name = models.CharField(max_length=255)
    beg_bal = models.BigIntegerField(default=0)
    incoming_bal = models.BigIntegerField(default=0)
    outgoing_bal = models.BigIntegerField(default=0)
    current_bal = models.BigIntegerField(default=0)
    actual_bal = models.BigIntegerField(default=0)
    loss = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    warehouse = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    product = models.ForeignKey(
        RawMaterial,
        on_delete=models.PROTECT,
        db_column="product_id",
        null=True,
        blank=True,
        related_name="product_inventory",
    )

    raw_material = models.ForeignKey(
        RawMaterial,
        on_delete=models.PROTECT,
        db_column="raw_material_id",
        related_name="inventories",
    )

    class Meta:
        db_table = "raw_materials_inventory"

    def __str__(self):
        return self.name
    

class FinishedProductInventory(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
    )

    name = models.CharField(max_length=255)
    beg_bal = models.BigIntegerField(default=0)
    incoming_bal = models.BigIntegerField(default=0)
    outgoing_bal = models.BigIntegerField(default=0)
    current_bal = models.BigIntegerField(default=0)
    actual_bal = models.BigIntegerField(default=0)
    loss = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    warehouse = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    finished_product = models.ForeignKey(
        FinishedProduct,
        on_delete=models.PROTECT,
        db_column="finished_product_id",
        related_name="inventories",
    )

    class Meta:
        db_table = "finished_products_inventory"

    def __str__(self):
        return self.name
    

class PackagingInventory(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
    )

    name = models.CharField(max_length=255)
    beg_bal = models.BigIntegerField(default=0)
    incoming_bal = models.BigIntegerField(default=0)
    outgoing_bal = models.BigIntegerField(default=0)
    current_bal = models.BigIntegerField(default=0)
    actual_bal = models.BigIntegerField(default=0)
    loss = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    warehouse = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    packaging = models.ForeignKey(
        Packaging,
        on_delete=models.PROTECT,
        db_column="packaging_id",
        related_name="inventories",
    )

    class Meta:
        db_table = "packaging_inventory"

    def __str__(self):
        return self.name