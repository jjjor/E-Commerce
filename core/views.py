from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView, View

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class ProductListView(ListView):

    template_name = 'products.html'
    model = Product
    context_object_name = 'products'

class ProductCreateView(CreateView):

    template_name = 'product_create.html'
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')

class ProductDeleteView(DeleteView):
    
        model = Product
        success_url = reverse_lazy('products')
        pk_url_kwarg = 'id'

        def get(self, *args, **kwargs):
            return self.delete(*args, **kwargs)

class ProductUpdateView(UpdateView):

    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy("products")