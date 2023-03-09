from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Beer

urlpatterns = [
    path('',
         ListView.as_view(
            queryset=
            Beer.objects.all(),
            template_name="shop.html"
            )),
    path('<int:pk>/',
         DetailView.as_view(
            model=Beer,
            template_name="beer.html"
            )),
    ]