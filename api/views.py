from django.shortcuts import render

def home(request):
    title = "This is homepage"
    context = {"title": title}
    return render(request, "home.html", context)

