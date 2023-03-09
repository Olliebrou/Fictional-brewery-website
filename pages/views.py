from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'entry.html')


def about(request):
    if request.user.is_authenticated:
        return render(request, 'about.html')
    else:
        return render(request, 'entry.html')


def products(request):
    if request.user.is_authenticated:
        return render(request, 'products.html')
    else:
        return render(request, 'entry.html')


def visit(request):
    if request.user.is_authenticated:
        return render(request, 'visit.html')
    else:
        return render(request, 'entry.html')
