from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Product


class ProductListView(ListView):
    template_name = "products/product-list.html"
    model = Product


class ProductDetailView(DetailView):
    template_name = "products/product-detail.html"
    model = Product


class ProductCreateView(CreateView):
    template_name = "products/product-create.html"
    model = Product
    fields = ['name', 'desc', 'purcheser']


class ProductUpdateView(UpdateView):
    template_name = "products/product-update.html"
    model = Product
    fields = ['name', 'desc', 'purcheser']


class ProductDeleteView(DeleteView):
    template_name = "products/product-delete.html"
    model = Product
    success_url = reverse_lazy("product_list")