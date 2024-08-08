from django.contrib import admin

from .forms import StockCreateForm
from .models import Stock  # Ensure you are using the correct relative import


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ["category", "item_name", "quantity"]
    form = StockCreateForm
    list_filter = ['category']

# Register your models here.
admin.site.register(Stock, StockCreateAdmin)
