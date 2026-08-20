import uuid

from django.db import models


class InventoryType(models.TextChoices):
    RAW_MATERIAL = "RAW_MATERIAL", "Raw Material"
    FINISHED_PRODUCT = "FINISHED_PRODUCT", "Finished Product"


class InventoryLedger(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventory_type = models.CharField(
        max_length=20,
        choices=InventoryType.choices,
    )
    inventory_id = models.UUIDField()
    inventory_date = models.DateField()
    field_changed = models.CharField(max_length=255)
    old_value = models.BigIntegerField(null=True, blank=True)
    new_value = models.BigIntegerField(null=True, blank=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.UUIDField(null=True, blank=True)

    class Meta:
        db_table = "inventory_ledger"

    def __str__(self):
        return f"{self.inventory_type} - {self.inventory_id}"


class UndoLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    undo_type = models.CharField(max_length=255, null=True, blank=True)
    tab = models.CharField(max_length=255, null=True, blank=True)
    snapshot = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = "undo_log"

    def __str__(self):
        return f"{self.undo_type} - {self.tab}"