from django.shortcuts import render, redirect, get_object_or_404
from master_data.models.finished_product import FinishedProduct
from master_data.forms.finished_product import FinishedProductForm
from master_data.services import finished_product

def finished_product_list(request):
  finished = finished_product.search_finished(
    request.GET.get('search')
  )

  return render(request,'products/home/finished_product.html', {
    'finished': finished,
  })

def finished_product_search(request):
  search = request.GET.get('search', '').strip()
  finished = finished_product.search_finished(search)

  return render(request, 'products/components/list/finished_product.html', {
    'finished': finished,
  })

def finished_product_new(request):
  form = FinishedProductForm(request.POST or None)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('finished_product_list')

  return render(request, 'products/new/finished_product.html', {
    'form': form,
  })

def finished_product_edit(request, id):
  finished = get_object_or_404(FinishedProduct, id=id)

  form = FinishedProductForm(request.POST or None, instance=finished)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('finished_product_list')

  return render(request, 'products/edit/finished_product.html', {
    'form': form,
    'finished': finished,
  })

def finished_product_delete(request, id):
  finished = get_object_or_404(FinishedProduct, id=id)

  if request.method == 'POST':
    finished.delete()
    return redirect('finished_product_list')

  return render(request, 'products/delete/finished_product.html', {
    'finished': finished,
  })