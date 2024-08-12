from django import forms
from django.core.exceptions import ValidationError

from .models import Stock


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category", "item_name", "quantity"]

    def clean_category(self):
        category = self.cleaned_data.get("category")
        item_name = self.cleaned_data.get("item_name")

        if not category:
            raise forms.ValidationError("This field is required.")

        # Check if the category exists and raise an error if it does
        if Stock.objects.filter(category=category).exists() and not self.instance.pk:
            raise forms.ValidationError(
                f"The category '{category}' already exists. You cannot create it again."
            )

        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get("item_name")
        category = self.cleaned_data.get("category")

        if not item_name:
            raise forms.ValidationError("This field is required.")

        # Ensure the item name is unique within the same category
        if (
            Stock.objects.filter(item_name=item_name, category=category).exists()
            and not self.instance.pk
        ):
            raise forms.ValidationError(
                f"The item name '{item_name}' already exists in the category '{category}'."
            )

        return item_name


class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category", "item_name"]


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category", "item_name", "quantity"]
