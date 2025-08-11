from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Brand, Product, Review, Flavour
# Register your models here.


class FlavourInline(admin.StackedInline):
    model = Flavour
    max_num = 1
    can_delete = False


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """ Product admin """
    list_display = ('name', 'brand', 'price', 'rating')
    search_fields = ('name', 'brand__name')
    text_fields = ('description', 'ingredients')
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [FlavourInline]  # Add this line


@admin.register(Brand)
class BrandAdmin(SummernoteModelAdmin):
    """ Brand admin """
    list_display = ('name',)
    search_fields = ('name',)
    text_fields = ('description',)
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """ Review admin """
    list_display = ('product', 'author', 'rating', 'created_on', 'approved')
    list_filter = ('product', 'created_on', 'approved')
    search_fields = ('product__name', 'author__username', 'comment')
    actions = ['approve_reviews']

    @admin.action(description="Approve selected reviews")
    def approve_reviews(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f"{updated} review(s) approved.")
