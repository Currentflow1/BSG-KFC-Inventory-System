import uuid
from django.db import models


class MonitoringEmployee(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    role = models.CharField(
        max_length=255,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "monitoring_employee"

    def __str__(self):
        return self.name


class RepresentativeEmployee(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    products = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "representative_employee"

    def __str__(self):
        return self.name


class StaffEmployee(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "staff_employee"

    def __str__(self):
        return self.name