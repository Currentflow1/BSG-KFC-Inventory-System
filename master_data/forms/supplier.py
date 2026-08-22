from django import forms
from master_data.models.supplier import Supplier

FIELD_CLASS = "w-full rounded-lg border px-4 py-2"

class SupplierForm(forms.ModelForm):

  class Meta:
    model = Supplier
    fields = [
      'company_name',
      'contact_person',
      'contact_title',
      'address',
      'city',
      'postal_code',
      'country',
      'phone_number',
      'fax',
    ]

    widgets = {
      'company_name': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
      'contact_person': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
      'contact_title': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
      'address': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
      'city': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
      'postal_code': forms.NumberInput(attrs={
        'class': FIELD_CLASS,
      }),
      'country': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
      'phone_number': forms.NumberInput(attrs={
        'class': FIELD_CLASS,
      }),
      'fax': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
    }