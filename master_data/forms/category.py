from django import forms
from master_data.models.category import Category

FIELD_CLASS = "w-full rounded-lg border px-4 py-2"

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = [
      'name',
      'description',
    ]

    widgets = {
      'name': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
      'description': forms.TextInput(attrs={
        'class': FIELD_CLASS,
      }),
    }