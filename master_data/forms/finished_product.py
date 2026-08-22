from django import forms
from master_data.models.finished_product import FinishedProduct

FIELD_CLASS_TEXT = "w-full rounded-lg border px-4 py-2"
FIELD_CLASS_SELECT = "w-50 rounded-lg border px-3 py-2"
FIELD_CLASS_CHECKBOX = "h-4 w-4 rounded border-gray-300"

class FinishedProductForm(forms.ModelForm):
  class Meta:
    model = FinishedProduct
    fields = [
      'name',
      'category',
      'low_stock_value',
      'discontinued',
    ]

    widgets = {
      'name': forms.TextInput(attrs={
        'class': FIELD_CLASS_TEXT,
      }),
      'category': forms.Select(attrs={
        'class': FIELD_CLASS_SELECT,
      }),
      'low_stock_value': forms.NumberInput(attrs={
        'class': FIELD_CLASS_TEXT,
      }),
      'discontinued': forms.Select(attrs={
        'class': FIELD_CLASS_CHECKBOX,
      }),
    }