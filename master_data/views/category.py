from django.shortcuts import render, redirect, get_object_or_404
from master_data.models.category import Category
from master_data.forms.category import CategoryForm
from master_data.services import category

def category_list(request):
  categories = category.search_category(
    request.GET.get('search')
  )

  return render(request,'category/home.html', {
    'categories': categories,
  })

def category_search(request):
  search = request.GET.get('search', '').strip()
  categories = category.search_category(search)

  return render(request, 'category/components/list.html', {
    'categories': categories,
  })

def category_new(request):
  form = CategoryForm(request.POST or None)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('category_list')

  return render(request, 'category/new.html', {
    'form': form,
  })

def category_edit(request, id):
  category = get_object_or_404(Category, id=id)

  form = CategoryForm(request.POST or None, instance=category)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('category_list')

  return render(request, 'category/edit.html', {
    'form': form,
    'category': category,
  })

def category_delete(request, id):
  category = get_object_or_404(Category, id=id)

  if request.method == 'POST':
    category.delete()
    return redirect('category_list')

  return render(request, 'category/delete.html', {
    'category': category,
  })