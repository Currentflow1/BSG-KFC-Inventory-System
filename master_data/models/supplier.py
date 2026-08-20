import uuid

from django.db import models


class Supplier(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    company_name = models.CharField(
        max_length=255,
        default="N/A",
    )

    contact_person = models.CharField(
        max_length=255,
        unique=True,
        default="N/A",
    )

    contact_title = models.CharField(
        max_length=255,
        default="N/A",
    )

    address = models.TextField(
        default="N/A",
    )

    city = models.CharField(
        max_length=255,
        default="N/A",
    )

    postal_code = models.BigIntegerField(
        null=True,
        blank=True,
    )

    country = models.CharField(
        max_length=255,
        default="N/A",
    )

    phone_number = models.CharField(
        max_length=255,
        default="N/A",
    )

    fax = models.CharField(
        max_length=255,
        default="N/A",
    )

    class Meta:
        db_table = "suppliers"

    def __str__(self):
        return self.company_name