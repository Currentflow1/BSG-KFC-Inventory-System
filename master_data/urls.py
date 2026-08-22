from django.urls import path
from master_data.views import category
from master_data.views import supplier
from master_data.views import employee
from master_data.views import raw_material
from master_data.views import packaging
from master_data.views import finished_product

urlpatterns = [
  #Categories
    path('category', category.category_list, name='category_list'),

    path('category/search/', category.category_search, name='category_search'),
    path('category/new/', category.category_new, name='category_new'),
    path('category/<uuid:id>/edit/', category.category_edit, name='category_edit'),
    path('category/<uuid:id>/delete/', category.category_delete, name='category_delete'),

  #Suppliers
    path('supplier', supplier.supplier_list, name='supplier_list'),
    
    path('supplier/search/', supplier.supplier_search, name='supplier_search'),
    path('supplier/new/', supplier.supplier_new, name='supplier_new'),
    path('supplier/<uuid:id>/edit/', supplier.supplier_edit, name='supplier_edit'),
    path('supplier/<uuid:id>/delete/', supplier.supplier_delete, name='supplier_delete'),

  #Employees
    path('employees/', employee.employee_list, name='employee_list'),
    path('employees/representatives/search/', employee.representative_search, name='representative_search'),
    path('employees/monitoring/search/', employee.monitoring_search, name='monitoring_search'),
    path('employees/staff/search/', employee.staff_search, name='staff_search'),

    path('employees/representatives/new/', employee.representative_new, name='representative_new'),
    path('employees/monitoring/new/', employee.monitoring_new, name='monitoring_new'),
    path('employees/staff/new/', employee.staff_new, name='staff_new'),

    path('employees/representatives/<uuid:id>/edit/', employee.representative_edit, name='representative_edit'),
    path('employees/monitoring/<uuid:id>/edit/', employee.monitoring_edit, name='monitoring_edit'),
    path('employees/staff/<uuid:id>/edit/', employee.staff_edit, name='staff_edit'),

    path('employees/representatives/<uuid:id>/delete/', employee.representative_delete, name='representative_delete'),
    path('employees/monitoring/<uuid:id>/delete/', employee.monitoring_delete, name='monitoring_delete'),
    path('employees/staff/<uuid:id>/delete/', employee.staff_delete, name='staff_delete'),

  #Raw
    path('raw_material', raw_material.raw_material_list, name='raw_material_list'),
    
    path('raw_material/search/', raw_material.raw_material_search, name='raw_material_search'),
    path('raw_material/new/', raw_material.raw_material_new, name='raw_material_new'),
    path('raw_material/<uuid:id>/edit/', raw_material.raw_material_edit, name='raw_material_edit'),
    path('raw_material/<uuid:id>/delete/', raw_material.raw_material_delete, name='raw_material_delete'),


  #Packaging
    path('packaging', packaging.packaging_list, name='packaging_list'),
    
    path('packaging/search/', packaging.packaging_search, name='packaging_search'),
    path('packaging/new/', packaging.packaging_new, name='packaging_new'),
    path('packaging/<uuid:id>/edit/', packaging.packaging_edit, name='packaging_edit'),
    path('packaging/<uuid:id>/delete/', packaging.packaging_delete, name='packaging_delete'),


  #Finished
    path('finished_product', finished_product.finished_product_list, name='finished_product_list'),
    
    path('finished_product/search/', finished_product.finished_product_search, name='finished_product_search'),
    path('finished_product/new/', finished_product.finished_product_new, name='finished_product_new'),
    path('finished_product/<uuid:id>/edit/', finished_product.finished_product_edit, name='finished_product_edit'),
    path('finished_product/<uuid:id>/delete/', finished_product.finished_product_delete, name='finished_product_delete'),
]