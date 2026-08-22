from django.db.models import Q
from master_data.models.category import Category

def search_category(search=None):
  categories = Category.objects.all()

  if search:
    categories = categories.filter(
      Q(name__icontains=search)
    )

  return categories