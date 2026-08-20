import uuid

from django.db import models

class Category(models.Model):
  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False,
  )

  name = models.CharField(max_length=255, unique=True)
  description = models.TextField(blank=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'categories'

  def __str__(self):
    return self.name

  