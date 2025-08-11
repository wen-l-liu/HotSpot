from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q, Count, Case, When, CharField, Value
from .models import Product, Review, Brand, Flavour
from .forms import ReviewForm, ProductForm

# Create your views here.


# class ProductListView(generic.ListView):
#     queryset = Product.objects.all()
#     paginate_by = 12
#     template_name = 'products/products_list.html'


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


@login_required
def product_edit(request, slug):
    """
    View to edit a product (admin/superuser only)
    """
    product = get_object_or_404(Product, slug=slug)
    
    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to edit products.')
        return redirect('product_detail', slug=slug)
    
    if request.method == 'POST':
        product_form = ProductForm(data=request.POST, files=request.FILES, instance=product)
        if product_form.is_valid():
            product = product_form.save()
            messages.success(request, f'Product "{product.name}" updated successfully!')
            return redirect('product_detail', slug=product.slug)
        else:
            messages.error(request, 'Error updating product. Please check the form.')
    else:
        product_form = ProductForm(instance=product)
    
    return render(
        request,
        'products/product_edit.html',
        {
            'product': product,
            'product_form': product_form,
        }
    )


class ProductList(generic.ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'product_list'
    paginate_by = 12

    def get_queryset(self):
        queryset = Product.objects.all()
        request = self.request

        # Search functionality
        search_query = request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(ingredients__icontains=search_query)
            )

        # Brand filtering (multi-select)
        brand_filters = request.GET.getlist('brand')
        if brand_filters and any(brand_filters):
            brand_q = Q()
            for brand_id in brand_filters:
                if brand_id:
                    brand_q |= Q(brand_id=brand_id)
            queryset = queryset.filter(brand_q)

        # Heat level filtering (multi-select)
        heat_filters = request.GET.getlist('heat')
        if heat_filters and any(heat_filters):
            heat_q = Q()
            for heat in heat_filters:
                if heat == 'low':
                    heat_q |= Q(flavours__heat__gte=0, flavours__heat__lte=3)
                elif heat == 'medium':
                    heat_q |= Q(flavours__heat__gte=4, flavours__heat__lte=6)
                elif heat == 'hot':
                    heat_q |= Q(flavours__heat__gte=7, flavours__heat__lte=10)
            queryset = queryset.filter(heat_q)

        # Flavour profile filtering (multi-select for each flavour)
        flavour_types = ['fruit', 'garlic', 'sweet', 'smoke', 'salt', 'vinegar']
        for flavour in flavour_types:
            flavour_filters = request.GET.getlist(flavour)
            if flavour_filters and any(flavour_filters):
                flavour_q = Q()
                for level in flavour_filters:
                    flavour_q |= Q(**{f"flavours__{flavour}": level})
                queryset = queryset.filter(flavour_q)

        return queryset.order_by('name')  # or 'created_on', 'id', etc.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request

        # For checkbox state
        context['selected_brands'] = request.GET.getlist('brand')
        context['selected_heats'] = request.GET.getlist('heat')
        context['brands'] = Brand.objects.all()

        # Build filtered queryset except for brand (for brand badge counts)
        filtered_queryset = Product.objects.all()

        # Apply search
        search_query = request.GET.get('search')
        if search_query:
            filtered_queryset = filtered_queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(ingredients__icontains=search_query)
            )

        # Apply heat filter
        heat_filters = request.GET.getlist('heat')
        if heat_filters and any(heat_filters):
            heat_q = Q()
            for heat in heat_filters:
                if heat == 'low':
                    heat_q |= Q(flavours__heat__gte=0, flavours__heat__lte=3)
                elif heat == 'medium':
                    heat_q |= Q(flavours__heat__gte=4, flavours__heat__lte=6)
                elif heat == 'hot':
                    heat_q |= Q(flavours__heat__gte=7, flavours__heat__lte=10)
            filtered_queryset = filtered_queryset.filter(heat_q)

        # Apply flavour filters
        flavour_types = ['fruit', 'garlic', 'sweet', 'smoke', 'salt', 'vinegar']
        for flavour in flavour_types:
            flavour_filters = request.GET.getlist(flavour)
            if flavour_filters and any(flavour_filters):
                flavour_q = Q()
                for level in flavour_filters:
                    flavour_q |= Q(**{f"flavours__{flavour}": level})
                filtered_queryset = filtered_queryset.filter(flavour_q)

        # --- Optimised Brand Counts ---
        brand_counts_qs = (
            filtered_queryset.values('brand')
            .annotate(count=Count('id'))
        )
        brand_count_map = {item['brand']: item['count'] for item in brand_counts_qs}
        context['brand_counts'] = brand_count_map

        # --- Optimised Flavour Counts ---
        intensity_levels = ['none', 'low', 'medium', 'high']
        flavour_options = [
            {'name': 'fruit', 'emoji': '🍓', 'display': 'Fruit'},
            {'name': 'garlic', 'emoji': '🧄', 'display': 'Garlic'},
            {'name': 'sweet', 'emoji': '🍯', 'display': 'Sweet'},
            {'name': 'smoke', 'emoji': '💨', 'display': 'Smoke'},
            {'name': 'salt', 'emoji': '🧂', 'display': 'Salt'},
            {'name': 'vinegar', 'emoji': '🥫', 'display': 'Vinegar'},
        ]

        # Build a dict of {flavour: {level: count}}
        flavour_counts = {}
        for flavour in flavour_types:
            level_counts = (
                filtered_queryset.values(f'flavours__{flavour}')
                .annotate(count=Count('id'))
            )
            level_map = {item[f'flavours__{flavour}']: item['count'] for item in level_counts}
            flavour_counts[flavour] = level_map

        for flavour in flavour_options:
            flavour['counts'] = {}
            for level in intensity_levels:
                flavour['counts'][level] = flavour_counts.get(flavour['name'], {}).get(level, 0)
        context['flavour_options'] = flavour_options
        context['intensity_levels'] = intensity_levels

        # For each flavour, add selected values to context
        selected_flavours = {}
        for flavour in flavour_types:
            selected_flavours[flavour] = request.GET.getlist(flavour)
        context['selected_flavours'] = selected_flavours

        # Optimised heat level counts
        heat_ranges = {
            'low': (0, 3),
            'medium': (4, 6),
            'hot': (7, 10),
        }
        heat_labels = {
            'low': '🌶️ Low Heat (0-3)',
            'medium': '🌶️🌶️ Medium Heat (4-6)',
            'hot': '🌶️🌶️🌶️ Hot (7-10)',
        }

        # Build Q objects for all heat levels and annotate in one query
        annotated_queryset = filtered_queryset.annotate(
            heat_level=Case(
                When(flavours__heat__gte=0, flavours__heat__lte=3, then=Value('low')),
                When(flavours__heat__gte=4, flavours__heat__lte=6, then=Value('medium')),
                When(flavours__heat__gte=7, flavours__heat__lte=10, then=Value('hot')),
                default=None,
                output_field=CharField(),
            )
        )

        heat_counts = (
            annotated_queryset.values('heat_level')
            .annotate(count=Count('id'))
        )

        heat_count_map = {item['heat_level']: item['count'] for item in heat_counts}

        context['heat_levels'] = [
            {
                'value': key,
                'label': heat_labels[key],
                'count': heat_count_map.get(key, 0)
            }
            for key in ['low', 'medium', 'hot']
        ]

        return context
