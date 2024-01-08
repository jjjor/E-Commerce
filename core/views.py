from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView, View

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class ProductListView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'
