from django import forms
from master_data.models.employee import StaffEmployee
from master_data.models.employee import MonitoringEmployee
from master_data.models.employee import RepresentativeEmployee

FIELD_CLASS = "w-full rounded-lg border px-4 py-2"

class MonitoringEmployeeForm(forms.ModelForm):

  class Meta:
    model = MonitoringEmployee
    fields = [
      'name',
      'role',
    ]

    widgets = {
      'name': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
      'role': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
    }


class RepresentativeEmployeeForm(forms.ModelForm):
  class Meta:
    model = RepresentativeEmployee
    fields = [
      'name',
      'products',
    ]

    widgets = {
      'name': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
      'products': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
    }


class StaffEmployeeForm(forms.ModelForm):
  class Meta:
    model = StaffEmployee
    fields = [
      'name',
    ]

    widgets = {
      'name': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
    }