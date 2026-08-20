import uuid

from django.db import models


class ProfileRole(models.TextChoices):
    ADMIN = "admin", "Admin"
    STAFF = "staff", "Staff"


class Profile(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    role = models.CharField(
        max_length=20,
        choices=ProfileRole.choices,
        default=ProfileRole.STAFF,
    )
    full_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "profiles"

    def __str__(self):
        return self.full_name or self.email or str(self.id)