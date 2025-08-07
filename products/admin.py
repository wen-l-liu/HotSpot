from django.contrib import admin
from .models import Brand, Product, Review
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """ Product admin """
    list_display = ('name', 'brand', 'price', 'rating')
    search_fields = ('name', 'brand__name')
    text_fields = ('description', 'ingredients')
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(SummernoteModelAdmin):
    """ Brand admin """
    list_display = ('name',)
    search_fields = ('name',)
    text_fields = ('description',)
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Review)
