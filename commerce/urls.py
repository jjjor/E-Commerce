"""
URL configuration for commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product_create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product_delete/<int:id>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('product_update/<int:id>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('category/', views.CategoryListView.as_view(), name='categories'),
    path('category_create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category_delete/<int:id>/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('category_update/<int:id>/', views.CategoryUpdateView.as_view(), name='category_update'),
]
