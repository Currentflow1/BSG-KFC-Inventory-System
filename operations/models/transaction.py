import uuid

from django.db import models

from master_data.models import (
    MonitoringEmployee,
    RepresentativeEmployee,
    Supplier,
)

from .inventory import (
    RawMaterialInventory,
    FinishedProductInventory,
    PackagingInventory,
)


class TransactionProcessingStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    PROCESSED = "processed", "Processed"
    FAILED = "failed", "Failed"


class TransactionSyncStatus(models.TextChoices):
    LOCAL = "local", "Local"
    SYNCING = "syncing", "Syncing"
    SYNCED = "synced", "Synced"
    SYNC_FAILED = "sync_failed", "Sync Failed"


class TransactionSource(models.TextChoices):
    ORDERED = "ordered", "Ordered"
    MANIPULATED = "manipulated", "Manipulated"


class TransactionType(models.TextChoices):
    STOCK_MOVEMENT = "stock_movement", "Stock Movement"
    COUNT_CORRECTION = "count_correction", "Count Correction"


class RemovedReason(models.TextChoices):
    DELETED = "deleted", "Deleted"
    UNDONE = "undone", "Undone"
    UNDONE_ITEM = "undone_item", "Undone Item"
    UNDONE_SESSION = "undone_session", "Undone Session"
    FINALIZE_REVERTED = "finalize_reverted", "Finalize Reverted"


class RawMaterialTransactionLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventory = models.ForeignKey(
        RawMaterialInventory,
        on_delete=models.PROTECT,
        db_column="inventory_id",
        related_name="transaction_logs",
    )
    monitoring_employee = models.ForeignKey(
        MonitoringEmployee,
        on_delete=models.PROTECT,
        to_field="name",
        db_column="monitoring_employee",
        related_name="raw_material_transactions",
    )
    representative_employee = models.ForeignKey(
        RepresentativeEmployee,
        on_delete=models.PROTECT,
        to_field="name",
        db_column="representative_employee",
        null=True,
        blank=True,
        related_name="raw_material_transactions",
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        to_field="contact_person",
        db_column="supplier_name",
        null=True,
        blank=True,
        related_name="raw_material_transactions",
    )
    product_name = models.CharField(max_length=255)
    incoming_bal = models.BigIntegerField(default=0)
    outgoing_bal = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField()
    finalized_at = models.DateTimeField(null=True, blank=True)
    created_by = models.UUIDField(null=True, blank=True)
    transaction_source = models.CharField(
        max_length=20,
        choices=TransactionSource.choices,
        default=TransactionSource.ORDERED,
    )
    actual_bal = models.BigIntegerField(null=True, blank=True)
    loss = models.BigIntegerField(null=True, blank=True)
    transaction_type = models.CharField(
        max_length=30,
        choices=TransactionType.choices,
        default=TransactionType.STOCK_MOVEMENT,
    )
    removed_at = models.DateTimeField(null=True, blank=True)
    removed_reason = models.CharField(
        max_length=30,
        choices=RemovedReason.choices,
        null=True,
        blank=True,
    )
    warehouse = models.CharField(max_length=255, null=True, blank=True)
    staff_employee = models.CharField(max_length=255, null=True, blank=True)
    processing_status = models.CharField(
        max_length=20,
        choices=TransactionProcessingStatus.choices,
        default=TransactionProcessingStatus.PENDING,
    )
    processed_at = models.DateTimeField(null=True, blank=True)
    failed_at = models.DateTimeField(null=True, blank=True)
    failure_reason = models.TextField(null=True, blank=True)
    sync_status = models.CharField(
        max_length=20,
        choices=TransactionSyncStatus.choices,
        default=TransactionSyncStatus.LOCAL,
    )

    class Meta:
        db_table = "raw_materials_transaction_log"

    def __str__(self):
        return f"{self.product_name} - {self.created_at}"


class FinishedProductTransactionLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventory = models.ForeignKey(
        FinishedProductInventory,
        on_delete=models.PROTECT,
        db_column="inventory_id",
        related_name="transaction_logs",
    )
    monitoring_employee = models.ForeignKey(
        MonitoringEmployee,
        on_delete=models.PROTECT,
        to_field="name",
        db_column="monitoring_employee",
        related_name="finished_product_transactions",
    )
    representative_employee = models.ForeignKey(
        RepresentativeEmployee,
        on_delete=models.PROTECT,
        to_field="name",
        db_column="representative_employee",
        null=True,
        blank=True,
        related_name="finished_product_transactions",
    )
    product_name = models.CharField(max_length=255)
    incoming_bal = models.BigIntegerField(default=0)
    outgoing_bal = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField()
    finalized_at = models.DateTimeField(null=True, blank=True)
    created_by = models.UUIDField(null=True, blank=True)
    transaction_source = models.CharField(
        max_length=20,
        choices=TransactionSource.choices,
        default=TransactionSource.ORDERED,
    )
    actual_bal = models.BigIntegerField(null=True, blank=True)
    loss = models.BigIntegerField(null=True, blank=True)
    transaction_type = models.CharField(
        max_length=30,
        choices=TransactionType.choices,
        default=TransactionType.STOCK_MOVEMENT,
    )
    removed_at = models.DateTimeField(null=True, blank=True)
    removed_reason = models.CharField(
        max_length=30,
        choices=RemovedReason.choices,
        null=True,
        blank=True,
    )
    warehouse = models.CharField(max_length=255, null=True, blank=True)
    staff_employee = models.CharField(max_length=255, null=True, blank=True)
    processing_status = models.CharField(
        max_length=20,
        choices=TransactionProcessingStatus.choices,
        default=TransactionProcessingStatus.PENDING,
    )
    processed_at = models.DateTimeField(null=True, blank=True)
    failed_at = models.DateTimeField(null=True, blank=True)
    failure_reason = models.TextField(null=True, blank=True)
    sync_status = models.CharField(
        max_length=20,
        choices=TransactionSyncStatus.choices,
        default=TransactionSyncStatus.LOCAL,
    )

    class Meta:
        db_table = "finished_products_transaction_log"

    def __str__(self):
        return f"{self.product_name} - {self.created_at}"


class PackagingTransactionLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventory = models.ForeignKey(
        PackagingInventory,
        on_delete=models.PROTECT,
        db_column="inventory_id",
        related_name="transaction_logs",
    )
    monitoring_employee = models.ForeignKey(
        MonitoringEmployee,
        on_delete=models.PROTECT,
        to_field="name",
        db_column="monitoring_employee",
        related_name="packaging_transactions",
    )
    representative_employee = models.ForeignKey(
        RepresentativeEmployee,
        on_delete=models.PROTECT,
        to_field="name",
        db_column="representative_employee",
        null=True,
        blank=True,
        related_name="packaging_transactions",
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        to_field="contact_person",
        db_column="supplier_name",
        null=True,
        blank=True,
        related_name="packaging_transactions",
    )
    product_name = models.CharField(max_length=255)
    incoming_bal = models.BigIntegerField(default=0)
    outgoing_bal = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField()
    finalized_at = models.DateTimeField(null=True, blank=True)
    created_by = models.UUIDField(null=True, blank=True)
    transaction_source = models.CharField(
        max_length=20,
        choices=TransactionSource.choices,
        default=TransactionSource.ORDERED,
    )
    actual_bal = models.BigIntegerField(null=True, blank=True)
    loss = models.BigIntegerField(null=True, blank=True)
    transaction_type = models.CharField(
        max_length=30,
        choices=TransactionType.choices,
        default=TransactionType.STOCK_MOVEMENT,
    )
    removed_at = models.DateTimeField(null=True, blank=True)
    removed_reason = models.CharField(
        max_length=30,
        choices=RemovedReason.choices,
        null=True,
        blank=True,
    )
    warehouse = models.CharField(max_length=255, null=True, blank=True)
    staff_employee = models.CharField(max_length=255, null=True, blank=True)
    processing_status = models.CharField(
        max_length=20,
        choices=TransactionProcessingStatus.choices,
        default=TransactionProcessingStatus.PENDING,
    )
    processed_at = models.DateTimeField(null=True, blank=True)
    failed_at = models.DateTimeField(null=True, blank=True)
    failure_reason = models.TextField(null=True, blank=True)
    sync_status = models.CharField(
        max_length=20,
        choices=TransactionSyncStatus.choices,
        default=TransactionSyncStatus.LOCAL,
    )

    class Meta:
        db_table = "packaging_transaction_log"

    def __str__(self):
        return f"{self.product_name} - {self.created_at}"