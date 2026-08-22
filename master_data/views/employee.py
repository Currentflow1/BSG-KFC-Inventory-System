from django.shortcuts import render, redirect, get_object_or_404
from master_data.models.employee import RepresentativeEmployee
from master_data.models.employee import MonitoringEmployee
from master_data.models.employee import StaffEmployee
from master_data.forms.employee import RepresentativeEmployeeForm
from master_data.forms.employee import MonitoringEmployeeForm
from master_data.forms.employee import StaffEmployeeForm
from master_data.services import employee

#Views for the list and searches

def employee_list(request):
    return render(request, 'employee/home.html', {
        'representatives': employee.search_representatives(),
        'monitorings': employee.search_monitoring(),
        'staffs': employee.search_staff(),
    })

def representative_search(request):
    search = request.GET.get('search', '').strip()
    representatives = employee.search_representatives(search)

    return render(request, 'employee/components/list/representative.html', {
        'representatives': representatives,
    })

def monitoring_search(request):
    search = request.GET.get('search', '').strip()
    monitorings = employee.search_monitoring(search)

    return render(request, 'employee/components/list/monitoring.html', {
        'monitorings': monitorings,
    })

def staff_search(request):
    search = request.GET.get('search', '').strip()
    staffs = employee.search_staff(search)

    return render(request, 'employee/components/list/staff.html', {
        'staffs': staffs,
    })

#Views for new entries(?)

def representative_new(request):
  form = RepresentativeEmployeeForm(request.POST or None)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('employee_list')

  return render(request, 'employee/new/representative.html', {
    'form': form,
  })

def monitoring_new(request):
  form = MonitoringEmployeeForm(request.POST or None)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('employee_list')

  return render(request, 'employee/new/monitoring.html', {
    'form': form,
  })

def staff_new(request):
  form = StaffEmployeeForm(request.POST or None)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('employee_list')

  return render(request, 'employee/new/staff.html', {
    'form': form,
  })

#Views for employee editing

def representative_edit(request, id):
  representative = get_object_or_404(RepresentativeEmployee, id=id)

  form = RepresentativeEmployeeForm(request.POST or None, instance=representative)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('employee_list')

  return render(request, 'employee/edit/representative.html', {
    'form': form,
    'representative': representative,
  })

def monitoring_edit(request, id):
  monitoring = get_object_or_404(MonitoringEmployee, id=id)

  form = MonitoringEmployeeForm(request.POST or None, instance=monitoring)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('employee_list')

  return render(request, 'employee/edit/monitoring.html', {
    'form': form,
    'monitoring': monitoring,
  })

def staff_edit(request, id):
  staff = get_object_or_404(StaffEmployee, id=id)

  form = StaffEmployeeForm(request.POST or None, instance=staff)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('employee_list')

  return render(request, 'employee/edit/staff.html', {
    'form': form,
    'staff': staff,
  })

#Views for deletion

def representative_delete(request, id):
  representative = get_object_or_404(RepresentativeEmployee, id=id)

  if request.method == 'POST':
    representative.delete()
    return redirect('employee_list')

  return render(request, 'employee/delete/representative.html', {
    'representative': representative,
  })

def monitoring_delete(request, id):
  monitoring = get_object_or_404(MonitoringEmployee, id=id)

  if request.method == 'POST':
    monitoring.delete()
    return redirect('employee_list')

  return render(request, 'employee/delete/monitoring.html', {
    'monitoring': monitoring,
  })

def staff_delete(request, id):
  staff = get_object_or_404(StaffEmployee, id=id)

  if request.method == 'POST':
    staff.delete()
    return redirect('employee_list')

  return render(request, 'employee/delete/staff.html', {
    'staff': staff,
  })