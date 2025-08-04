from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Product
# Create your views here.


class ProductListView(generic.ListView):
    queryset = Product.objects.all()
    paginate_by = 12
    template_name = 'products/products_list.html'


def product_detail(request, slug):
    """
    Display an individual :model:`products.Product`.

    **Context**

    ``product``
        An instance of :model:`products.Product`.
    ``comments``
        A list of approved comments related to the product.
    ``comment_form``
        An instance of :form:`products.CommentForm`.
    **Template:**

    :template:`products/product_detail.html`
    """

    queryset = Product.objects.all()
    product = get_object_or_404(queryset, slug=slug)
    # comments = product.comments.all().order_by("-created_on")
    # comment_count = product.comments.filter(approved=True).count()
    # if request.method == "POST":
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         comment = comment_form.save(commit=False)
    #         comment.author = request.user
    #         comment.post = post
    #         comment.save()
    #         messages.add_message(
    #             request, messages.SUCCESS,
    #             'Comment submitted and awaiting approval'
    #         )
    # comment_form = CommentForm()

    return render(
        request,
        "blog/product_detail.html",
        {
            "product": product,
            # "comments": comments,
            # "comment_count": comment_count,
            # "comment_form": comment_form,
        },
    )
