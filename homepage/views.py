from django.views import generic
from products.models import Product

# Create your views here.


class HomepageView(generic.ListView):
    queryset = Product.objects.order_by('-created_on')[:8]
    template_name = "homepage/index.html"
