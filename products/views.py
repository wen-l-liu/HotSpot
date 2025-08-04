from django.shortcuts import render
from django.views import generic
from .models import Product
# Create your views here.


class ProductListView(generic.ListView):
    queryset = Product.objects.all()
    paginate_by = 8
    template_name = 'products/products_list.html'
