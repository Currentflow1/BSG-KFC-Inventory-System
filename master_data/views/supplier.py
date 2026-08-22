from django.shortcuts import render, redirect, get_object_or_404
from master_data.models.supplier import Supplier
from master_data.forms.supplier import SupplierForm
from master_data.services import supplier

def supplier_list(request):
  categories = supplier.search_supplier(
    request.GET.get('search')
  )

  return render(request,'supplier/home.html', {
    'categories': categories,
  })

def supplier_search(request):
  search = request.GET.get('search', '').strip()
  categories = supplier.search_supplier(search)

  return render(request, 'supplier/components/list.html', {
    'categories': categories,
  })

def supplier_new(request):
  form = SupplierForm(request.POST or None)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('supplier_list')

  return render(request, 'supplier/new.html', {
    'form': form,
  })

def supplier_edit(request, id):
  supplier = get_object_or_404(Supplier, id=id)

  form = SupplierForm(request.POST or None, instance=supplier)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('supplier_list')

  return render(request, 'supplier/edit.html', {
    'form': form,
    'supplier': supplier,
  })

def supplier_delete(request, id):
  supplier = get_object_or_404(Supplier, id=id)

  if request.method == 'POST':
    supplier.delete()
    return redirect('supplier_list')

  return render(request, 'supplier/delete.html', {
    'supplier': supplier,
  })