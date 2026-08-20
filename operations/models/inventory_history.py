import uuid

from django.db import models

from .inventory import (
    RawMaterialInventory,
    FinishedProductInventory,
    PackagingInventory,
)


class RawMaterialInventoryHistory(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    inventory = models.ForeignKey(
        RawMaterialInventory,
        on_delete=models.CASCADE,
        db_column="inventory_id",
        related_name="history",
    )

    inventory_date = models.DateField()

    name = models.CharField(
        max_length=255,
    )

    beg_bal = models.BigIntegerField(default=0)
    incoming_bal = models.BigIntegerField(default=0)
    outgoing_bal = models.BigIntegerField(default=0)
    current_bal = models.BigIntegerField(default=0)
    actual_bal = models.BigIntegerField(default=0)
    loss = models.BigIntegerField(default=0)

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    warehouse = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "raw_materials_inventory_history"

    def __str__(self):
        return f"{self.name} - {self.inventory_date}"


class FinishedProductInventoryHistory(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    inventory = models.ForeignKey(
        FinishedProductInventory,
        on_delete=models.CASCADE,
        db_column="inventory_id",
        related_name="history",
    )

    inventory_date = models.DateField()

    name = models.CharField(
        max_length=255,
    )

    beg_bal = models.BigIntegerField(default=0)
    incoming_bal = models.BigIntegerField(default=0)
    outgoing_bal = models.BigIntegerField(default=0)
    current_bal = models.BigIntegerField(default=0)
    actual_bal = models.BigIntegerField(default=0)
    loss = models.BigIntegerField(default=0)

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    warehouse = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "finished_products_inventory_history"

    def __str__(self):
        return f"{self.name} - {self.inventory_date}"


class PackagingInventoryHistory(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    inventory = models.ForeignKey(
        PackagingInventory,
        on_delete=models.CASCADE,
        db_column="inventory_id",
        related_name="history",
    )

    inventory_date = models.DateField()

    name = models.CharField(
        max_length=255,
    )

    beg_bal = models.BigIntegerField(default=0)
    incoming_bal = models.BigIntegerField(default=0)
    outgoing_bal = models.BigIntegerField(default=0)
    current_bal = models.BigIntegerField(default=0)
    actual_bal = models.BigIntegerField(default=0)
    loss = models.BigIntegerField(default=0)

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    warehouse = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "packaging_inventory_history"

    def __str__(self):
        return f"{self.name} - {self.inventory_date}"