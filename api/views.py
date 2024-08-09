from django.shortcuts import redirect, render

from .forms import StockCreateForm, StockSearchForm
from .models import Stock


def home(request):
    title = "This is homepage"
    context = {"title": title}
    return render(request, "home.html", context)


def list_items(request):
    header = "List of items"
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {"header": header, "queryset": queryset, "form": form}
    if request.method == "POST":
        queryset = Stock.objects.filter(
            category__icontains=form["category"].value(),
            item_name__icontains=form["item_name"].value(),
        )
        context = {"form": form, "header": header, "queryset": queryset}

    return render(request, "list_items.html", context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/list_items")
    context = {"form": form, "title": "Add item"}
    return render(request, "add_items.html", context)
