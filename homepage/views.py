from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from products.models import Product

# Create your views here.


class HomepageView(generic.ListView):
    queryset = Product.objects.all()
    template_name = "homepage/index.html"
