from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Product, Review
from .forms import ReviewForm
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
    ``reviews``
        A list of approved reviews related to the product.
    ``review_form``
        An instance of :form:`products.reviewForm`.
    **Template:**

    :template:`products/product_detail.html`
    """
    print("Product detail view accessed")
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, slug=slug)
    reviews = product.reviews.all().order_by("-created_on")
    review_count = product.reviews.filter(approved=True).count()
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'review submitted and awaiting approval'
            )
    review_form = ReviewForm()
    print("Product detail mid")
    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "reviews": reviews,
            "review_count": review_count,
            "review_form": review_form,
        },
    )


def review_edit(request, slug, review_id):
    """
    Display an individual :model:`blog.review` for editing.
    **Context:**
    ``post``
        An instance of :model:`blog.Post`.
        ``review``
        An instance of :model:`blog.review`.
    ``comment_form``
        An instance of :form:`blog.CommentForm` pre-populated with the review.
    """
    if request.method == "POST":

        queryset = Product.objects.all()
        product = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.product = product
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'review Updated!')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error updating review!')

    return HttpResponseRedirect(reverse('product_detail', args=[slug]))


def review_delete(request, slug, review_id):
    """
    View to delete review
    """
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own reviews!'
        )

    return HttpResponseRedirect(reverse('product_detail', args=[slug]))  # Fixed: product_detail not post_detail
