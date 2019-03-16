from django.shortcuts import render


# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html", {'title': 'Home'})


def about(request):
    """A view that displays the index page"""
    return render(request, "about.html", {'title': 'About'})
