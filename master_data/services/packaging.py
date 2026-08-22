from django.db.models import Q
from master_data.models.packaging import Packaging

def search_packaging(search=None):
  packaging = Packaging.objects.all()

  if search:
    packaging = packaging.filter(
      Q(name__icontains=search) |
      Q(supplier__icontains=search)
    )

  return packaging