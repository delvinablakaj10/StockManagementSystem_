from django.contrib import admin

from .forms import StockCreateForm
from .models import Category, Stock


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ["category", "item_name", "quantity"]
    form = StockCreateForm
    list_filter = ["category"]


# Register your models here.
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)
