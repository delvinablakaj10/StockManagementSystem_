from django.shortcuts import redirect, render

from .forms import StockCreateForm
from .models import Stock


def home(request):
    title = "This is homepage"
    context = {"title": title}
    return render(request, "home.html", context)


def list_items(request):
    title = "List of items"
    queryset = Stock.objects.all()
    context = {"title": title, "queryset": queryset}
    return render(request, "list_items.html", context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/list_items")
    context = {"form": form, "title": "Add item"}
    return render(request, "add_items.html", context)
