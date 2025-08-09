from django.contrib import admin
from .models import Brand, Product, Review, Flavour  # Make sure Flavour is imported
from django_summernote.admin import SummernoteModelAdmin

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


admin.site.register(Review)
