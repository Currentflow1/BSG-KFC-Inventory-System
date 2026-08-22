from django.db.models import Q
from master_data.models.employee import RepresentativeEmployee
from master_data.models.employee import MonitoringEmployee
from master_data.models.employee import StaffEmployee

def search_representatives(search=None):
  representatives = RepresentativeEmployee.objects.all()

  if search:
    representatives = representatives.filter(
      Q(name__icontains=search) |
      Q(products__icontains=search) 
    )

  return representatives

def search_monitoring(search=None):
  monitorings = MonitoringEmployee.objects.all()

  if search:
    monitorings = monitorings.filter(
      Q(name__icontains=search) |
      Q(role__icontains=search)
    )

  return monitorings

def search_staff(search=None):
  staff = StaffEmployee.objects.all()

  if search:
    staff = staff.filter(
      Q(name__icontains=search)
    )

  return staff