from django.db.models import Q
from master_data.models.raw_material import RawMaterial

def search_raw(search=None):
  raw = RawMaterial.objects.all()

  if search:
    raw = raw.filter(
      Q(name__icontains=search) |
      Q(supplier__icontains=search)
    )

  return raw