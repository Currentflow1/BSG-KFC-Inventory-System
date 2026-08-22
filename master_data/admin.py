from django.contrib import admin
from master_data.models import Category
from master_data.models import MonitoringEmployee
from master_data.models import RepresentativeEmployee
from master_data.models import StaffEmployee
from master_data.models import RawMaterial
from master_data.models import Packaging
from master_data.models import FinishedProduct
from master_data.models import Supplier

admin.site.register(Category)
admin.site.register(MonitoringEmployee)
admin.site.register(RepresentativeEmployee)
admin.site.register(StaffEmployee)
admin.site.register(RawMaterial)
admin.site.register(Packaging)
admin.site.register(FinishedProduct)
admin.site.register(Supplier)