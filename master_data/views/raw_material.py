from django.shortcuts import render, redirect, get_object_or_404
from master_data.models.raw_material import RawMaterial
from master_data.forms.raw_material import RawMaterialForm
from master_data.services import raw_material

def raw_material_list(request):
  raw = raw_material.search_raw(
    request.GET.get('search')
  )

  return render(request,'products/home/raw_material.html', {
    'raw': raw,
  })

def raw_material_search(request):
  search = request.GET.get('search', '').strip()
  raw = raw_material.search_raw(search)

  return render(request, 'products/components/list/raw_material.html', {
    'raw': raw,
  })

def raw_material_new(request):
  form = RawMaterialForm(request.POST or None)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('raw_material_list')

  return render(request, 'products/new/raw_material.html', {
    'form': form,
  })

def raw_material_edit(request, id):
  raw = get_object_or_404(RawMaterial, id=id)

  form = RawMaterialForm(request.POST or None, instance=raw)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('raw_material_list')

  return render(request, 'products/edit/raw_material.html', {
    'form': form,
    'raw': raw,
  })

def raw_material_delete(request, id):
  raw = get_object_or_404(RawMaterial, id=id)

  if request.method == 'POST':
    raw.delete()
    return redirect('raw_material_list')

  return render(request, 'products/delete/raw_material.html', {
    'raw': raw,
  })