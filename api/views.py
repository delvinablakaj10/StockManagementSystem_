import csv

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import StockCreateForm, StockSearchForm, StockUpdateForm
from .models import Stock
from django.contrib import messages


def home(request):
    title = "This is homepage"
    context = {"title": title}
    return render(request, "home.html", context)


def list_items(request):
    header = "List of items"
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    if request.method == "POST":
        queryset = Stock.objects.filter(
            category__name__icontains=form["category"].value(),
            item_name__icontains=form["item_name"].value(),
        )
    if form["export_to_CSV"].value() == True:
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="List of stock.csv"'
        writer = csv.writer(response)
        writer.writerow(["CATEGORY", "ITEM NAME", "QUANTITY"])
        instance = queryset
        for stock in instance:
            writer.writerow([stock.category, stock.item_name, stock.quantity])
        return response
    context = {"form": form, "header": header, "queryset": queryset}

    return render(request, "list_items.html", context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully added")

        return redirect("/list_items")
    context = {"form": form, "title": "Add item"}
    return render(request, "add_items.html", context)


def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(request.POST or None)
    context = {"queryset": queryset, "form": form}
    if request.method == "POST":
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated")

            return redirect("/list_items")
        context = {"form": form}

    return render(request, "add_items.html", context)


def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        messages.success(request, "Deleted successfully")
        return redirect("/list_items")
    return render(request, "delete_items.html")
