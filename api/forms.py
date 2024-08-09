from django import forms
from django.core.exceptions import ValidationError

from .models import Stock


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category", "item_name", "quantity"]

    def clean_category(self):
        category = self.cleaned_data.get("category")
        if not category:
            raise forms.ValidationError("This field is required")

        # Use exists() to check for the existence of the category more efficiently
        if Stock.objects.filter(category=category).exists():
            raise forms.ValidationError(f"{category} is already created")

        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get("item_name")
        if not item_name:
            raise forms.ValidationError("This field is required")
        if Stock.objects.filter(item_name=item_name).exists():
            raise forms.ValidationError(f"The item name '{item_name}' already exists.")
        return item_name


class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category", "item_name"]
