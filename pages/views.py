from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    """
    View function in the pages app used to render the index page if the user is logged in or the entry page if not

    :param request: Httprequest object

    :returns: HttpResponse object containing an HTML response of the index HTML if the user is logged in
    and the entry HTML if the user is not logged in

    :rtype: HttpResponse object containing an HTML response

    """
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'entry.html')


def about(request):
    """
    View function in the pages app used to render the about page if the user is logged in or the entry page if not

    :param request: Httprequest object

    :returns: HttpResponse object containing an HTML response of the about.html template if the user is logged in
    and the entry.html if the user is not logged in

    :rtype: HttpResponse object containing an HTML response

    """
    if request.user.is_authenticated:
        return render(request, 'about.html')
    else:
        return render(request, 'entry.html')


def products(request):
    """
    View function in the pages app used to render the products.html template if the user is logged in or the entry page if not

    :param request: Httprequest object

    :returns: HttpResponse object containing an HTML response of the products.html template if the user is logged in
    and the entry.html if the user is not logged in

    :rtype: HttpResponse object containing an HTML response

    """
    if request.user.is_authenticated:
        return render(request, 'products.html')
    else:
        return render(request, 'entry.html')


def visit(request):
    """View function in the pages app used to render the visit.html page if the user is logged in or the entry page if not

    :param request: Httprequest object

    :returns: HttpResponse object containing an HTML response of the visit.html template if the user is logged in
    and the entry.html if the user is not logged in

    :rtype: HttpResponse object containing an HTML response

    """
    if request.user.is_authenticated:
        return render(request, 'visit.html')
    else:
        return render(request, 'entry.html')

