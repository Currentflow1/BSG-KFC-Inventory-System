from django.db.models import Q
from master_data.models.supplier import Supplier

def search_supplier(search=None):
  categories = Supplier.objects.all()

  if search:
    categories = categories.filter(
      Q(company_name__icontains=search) |
      Q(contact_person__icontains=search) |
      Q(contact_title__icontains=search) |
      Q(address__icontains=search) |
      Q(city__icontains=search) |
      Q(postal_code__icontains=search) |
      Q(country__icontains=search) |
      Q(phone_number__icontains=search) |
      Q(fax__icontains=search) 
    )

  return categories