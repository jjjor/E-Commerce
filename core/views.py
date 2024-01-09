from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView, View

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context


class ProductListView(ListView):

    template_name = 'products.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context
    
    # def get_queryset(self):
    #     query = self.request.GET.get('search')

    #     if query:
    #         queryset = Product.objects.filter(name_icontains=query)
    #     else:
    #         queryset = Product.objects.all()

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
    
class CategoryListView(ListView):

    model = Category
    template_name = 'categories.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorys"] = Category.objects.all()
        return context
    

class CategoryCreateView(CreateView):

    model = Category
    template_name = 'category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories')

class CategoryUpdateView(UpdateView):
         
        model = Category
        template_name = 'category_create.html'
        form_class = CategoryForm
        pk_url_kwarg = 'id'
    
        def get_success_url(self):
            return reverse_lazy("categories")

class CategoryDeleteView(DeleteView):

    model = Category
    success_url = reverse_lazy('categories')
    pk_url_kwarg = 'id'

    def get(self, *args, **kwargs):
            return self.delete(*args, **kwargs)
    

    
