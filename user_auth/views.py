from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

def register(request):
    """
    View function for registering a new user.

    If the request method is POST, the function will validate the form and
    create a new user if the form is valid. The user will then be authenticated
    and redirected to the home page. If the request method is not POST, the
    function will display the registration form.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: The rendered HTML template for the registration page, along with the registration form.
    :rtype: HttpResponse

    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Get the username and password from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authenticate the user and log them in
            user = authenticate(request, username=username, password=password)
            login(request, user)
            # Redirect to the home page or some other page
            return HttpResponseRedirect(reverse('pages:index'))
    else:
        form = RegisterForm()
    return render(request, 'authentication/register.html', {'form': form})



def login_view(request):
    """
    View function for handling user login.
    If the request method is POST, validate the form data and log in the user if
    the credentials are valid. Otherwise, display the login form.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object.
    :rtype: HttpResponse

    """
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('pages:index'))
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('pages:index')