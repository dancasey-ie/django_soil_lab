from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "home.html")

def about(request):
    """A view that displays the index page"""
    return render(request, "about.html")