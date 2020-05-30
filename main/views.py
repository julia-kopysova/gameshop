from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
#from .models import
from django.views.generic import ListView,DetailView


class HomeView(ListView):
    #model = Sight
    template_name = "home.html"
