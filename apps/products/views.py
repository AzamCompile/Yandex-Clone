from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import ProductForm
from .models import Product


def home(request):
    return render(request, 'products/home.html')


class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product_list.html'



class CreateProduct(CreateView):
    form_class = ProductForm
    template_name = 'products/create_product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products')



class UpdateProduct(UpdateView):
    form_class = ProductForm
    template_name = 'products/update_product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')
    pk_url_kwarg = 'pk'



class DeleteProduct(DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('product_list')

