from django.db.models import Q
from master_data.models.finished_product import FinishedProduct

def search_finished(search=None):
  finished = FinishedProduct.objects.all()

  if search:
    finished = finished.filter(
      Q(name__icontains=search)
    )

  return finished