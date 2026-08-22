from django.shortcuts import render, redirect, get_object_or_404
from master_data.models.packaging import Packaging
from master_data.forms.packaging import PackagingForm
from master_data.services import packaging as packaging_service

def packaging_list(request):
  packaging = packaging_service.search_packaging(
    request.GET.get('search')
  )

  return render(request,'products/home/packaging.html', {
    'packaging': packaging,
  })

def packaging_search(request):
  search = request.GET.get('search', '').strip()
  packaging = packaging_service.search_packaging(search)

  return render(request, 'products/components/list/packaging.html', {
    'packaging': packaging,
  })

def packaging_new(request):
  form = PackagingForm(request.POST or None)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('packaging_list')

  return render(request, 'products/new/packaging.html', {
    'form': form,
  })

def packaging_edit(request, id):
  packaging = get_object_or_404(Packaging, id=id)

  form = PackagingForm(request.POST or None, instance=packaging)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('packaging_list')

  return render(request, 'products/edit/packaging.html', {
    'form': form,
    'packaging': packaging,
  })

def packaging_delete(request, id):
  packaging = get_object_or_404(Packaging, id=id)

  if request.method == 'POST':
    packaging.delete()
    return redirect('packaging_list')

  return render(request, 'products/delete/packaging.html', {
    'packaging': packaging,
  })