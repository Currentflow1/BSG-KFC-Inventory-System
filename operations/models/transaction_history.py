import uuid

from django.db import models

from .transaction import (
    RawMaterialTransactionLog,
    FinishedProductTransactionLog,
    PackagingTransactionLog,
)


class RawMaterialTransactionLogHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source_log = models.ForeignKey(
        RawMaterialTransactionLog,
        on_delete=models.SET_NULL,
        db_column="source_log_id",
        null=True,
        blank=True,
        related_name="history_records",
    )
    log_date = models.DateField()
    inventory_id = models.UUIDField()
    monitoring_employee = models.CharField(max_length=255, null=True, blank=True)
    representative_employee = models.CharField(max_length=255, null=True, blank=True)
    supplier_name = models.CharField(max_length=255, null=True, blank=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    incoming_bal = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    outgoing_bal = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    archived_at = models.DateTimeField(auto_now_add=True)
    created_by = models.UUIDField(null=True, blank=True)
    warehouse = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "raw_materials_transaction_log_history"

    def __str__(self):
        return f"{self.product_name} - {self.log_date}"


class FinishedProductTransactionLogHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source_log = models.ForeignKey(
        FinishedProductTransactionLog,
        on_delete=models.SET_NULL,
        db_column="source_log_id",
        null=True,
        blank=True,
        related_name="history_records",
    )
    log_date = models.DateField()
    inventory_id = models.UUIDField()
    monitoring_employee = models.CharField(max_length=255, null=True, blank=True)
    representative_employee = models.CharField(max_length=255, null=True, blank=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    incoming_bal = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    outgoing_bal = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    archived_at = models.DateTimeField(auto_now_add=True)
    created_by = models.UUIDField(null=True, blank=True)
    warehouse = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "finished_products_transaction_log_history"

    def __str__(self):
        return f"{self.product_name} - {self.log_date}"


class PackagingTransactionLogHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source_log = models.ForeignKey(
        PackagingTransactionLog,
        on_delete=models.SET_NULL,
        db_column="source_log_id",
        null=True,
        blank=True,
        related_name="history_records",
    )
    log_date = models.DateField()
    inventory_id = models.UUIDField()
    monitoring_employee = models.CharField(max_length=255, null=True, blank=True)
    representative_employee = models.CharField(max_length=255, null=True, blank=True)
    supplier_name = models.CharField(max_length=255, null=True, blank=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    incoming_bal = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    outgoing_bal = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    archived_at = models.DateTimeField(auto_now_add=True)
    created_by = models.UUIDField(null=True, blank=True)
    warehouse = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "packaging_transaction_log_history"

    def __str__(self):
        return f"{self.product_name} - {self.log_date}"